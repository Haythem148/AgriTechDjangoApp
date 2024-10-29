from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Count, Q, DecimalField, Avg, FloatField,IntegerField
from django.db.models.functions import Coalesce
from .models import Farm, Crop
from .ai.models import CropHealthPredictor
from .ai.risk_analyzer import FarmRiskAnalyzer

class FarmListView(ListView):
    model = Farm
    template_name = 'farms/farm_list.html'
    context_object_name = 'farms'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate farm statistics with proper decimal field specification
        farms_data = Farm.objects.aggregate(
            total_area=Sum('area'),  # No need for Coalesce since area is required
            total_crops=Count('crops')
        )
        
        context.update({
            'total_area': round(farms_data['total_area'] or 0, 2),  # Handle None case
            'total_crops': farms_data['total_crops']
        })

        return context

class FarmDetailView(DetailView):
    model = Farm
    template_name = 'farms/farm_detail.html'
    context_object_name = 'farm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        farm = self.get_object()
        
        # Get crop statistics
        context['crop_stats'] = {
            'total_crops': farm.crops.count(),
            'total_area': farm.crops.aggregate(total=Sum('area'))['total'] or 0,
            'avg_health': farm.crops.aggregate(avg=Avg('health'))['avg'] or 0,
            
            # Add distribution data
            'crop_types': [
                {'type': type_name, 'count': count}
                for type_name, count in farm.crops.values('crop_type')
                .annotate(count=Count('id'))
                .values_list('crop_type', 'count')
            ],
            'growth_stages': [
                {'growth_stage': stage_name, 'count': count}
                for stage_name, count in farm.crops.values('growth_stage')
                .annotate(count=Count('id'))
                .values_list('growth_stage', 'count')
            ]
        }
        
        # Initialize AI components
        predictor = CropHealthPredictor()
        risk_analyzer = FarmRiskAnalyzer()
        
        # Process each crop
        ai_insights = []
        for crop in farm.crops.all():
            crop_insights = {
                'crop_name': crop.name,
                'current_health': crop.health,
                'predicted_health': predictor.predict_health(crop),
                'risks': risk_analyzer.analyze_crop_risks(crop),
                'optimization_suggestions': self.get_optimization_suggestions(crop)
            }
            ai_insights.append(crop_insights)
        
        context['ai_insights'] = ai_insights
        return context

    def optimize_water_usage(self, crop):
        # Calculate optimal water usage based on crop type and growth stage
        base_requirement = float(crop.water_requirements)
        stage_multiplier = {
            'SEEDLING': 0.7,
            'VEGETATIVE': 1.0,
            'FLOWERING': 1.2,
            'FRUITING': 1.1,
            'MATURE': 0.8
        }
        
        optimal_usage = base_requirement * stage_multiplier.get(crop.growth_stage, 1.0)
        return {
            'current_usage': base_requirement,
            'optimal_usage': round(optimal_usage, 2),
            'savings_potential': round(max(0, base_requirement - optimal_usage), 2)
        }

    def optimize_fertilizer_schedule(self, crop):
        # Calculate optimal fertilizer schedule based on growth stage
        current_requirement = float(crop.fertilizer_requirements)
        days_to_harvest = (crop.expected_harvest_date - crop.planting_date).days
        
        return {
            'next_application': f"In {max(0, min(7, days_to_harvest))} days",
            'recommended_amount': f"{round(current_requirement * 0.8, 2)} kg/ha",
            'frequency': "Weekly"
        }

    def predict_optimal_harvest(self, crop):
        # Predict optimal harvest time based on growth stage and health
        days_to_harvest = (crop.expected_harvest_date - crop.planting_date).days
        
        if crop.health < 60:
            adjustment = "Consider early harvest"
        elif crop.health > 80:
            adjustment = "Optimal conditions"
        else:
            adjustment = "Monitor closely"
            
        return {
            'predicted_date': crop.expected_harvest_date,
            'days_remaining': days_to_harvest,
            'recommendation': adjustment
        }

    def get_optimization_suggestions(self, crop):
        return {
            'water_optimization': self.optimize_water_usage(crop),
            'fertilizer_planning': self.optimize_fertilizer_schedule(crop),
            'harvest_timing': self.predict_optimal_harvest(crop)
        }

class FarmCreateView(SuccessMessageMixin, CreateView):
    model = Farm
    template_name = 'farms/farm_form.html'
    fields = ['name', 'location', 'area', 'latitude', 'longitude']
    success_url = reverse_lazy('farms:farm-list')
    success_message = "Farm was created successfully"

class FarmUpdateView(SuccessMessageMixin, UpdateView):
    model = Farm
    template_name = 'farms/farm_form.html'
    fields = ['name', 'location', 'area', 'latitude', 'longitude']
    success_message = "Farm was updated successfully"
    def get_success_url(self):
        return reverse_lazy('farms:farm-detail', kwargs={'pk': self.object.pk})

class FarmDeleteView(DeleteView):
    model = Farm
    template_name = 'farms/farm_confirm_delete.html'
    success_url = reverse_lazy('farms:farm-list')

class CropListView(ListView):
    model = Crop
    template_name = 'farms/crop_list.html'
    context_object_name = 'crops'
    paginate_by = 10

    def get_queryset(self):
        self.farm = get_object_or_404(Farm, pk=self.kwargs['farm_pk'])
        return Crop.objects.filter(farm=self.farm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['farm'] = self.farm
        return context

class CropDetailView(DetailView):
    model = Crop
    template_name = 'farms/crop_detail.html'
    context_object_name = 'crop'

class CropCreateView(SuccessMessageMixin, CreateView):
    model = Crop
    template_name = 'farms/crop_form.html'
    fields = [
        'name',
        'crop_type',
        'growth_stage',
        'area',
        'water_requirements',
        'fertilizer_requirements',
        'planting_date',
        'expected_harvest_date',
        'health',
        'notes'
    ]
    success_message = "Crop was created successfully"

    def get_success_url(self):
        return reverse_lazy('farms:farm-detail', kwargs={'pk': self.kwargs['farm_pk']})

    def form_valid(self, form):
        form.instance.farm = get_object_or_404(Farm, pk=self.kwargs['farm_pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['farm'] = get_object_or_404(Farm, pk=self.kwargs['farm_pk'])
        return context

class CropUpdateView(SuccessMessageMixin, UpdateView):
    model = Crop
    template_name = 'farms/crop_form.html'
    fields = ['name', 'crop_type', 'growth_stage', 'area', 'water_requirements', 
              'fertilizer_requirements', 'planting_date', 'expected_harvest_date', 
              'health', 'notes']
    success_message = "Crop was updated successfully"

    def get_success_url(self):
        return reverse_lazy('farms:crop-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['farm'] = self.object.farm
        return context

class CropDeleteView(DeleteView):
    model = Crop
    template_name = 'farms/crop_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('farms:crop-list', kwargs={'farm_pk': self.object.farm.pk})
