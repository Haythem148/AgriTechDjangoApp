from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Avg
from .models import TypeDechet, PlanGestionDechets
from .forms import TypeDechetForm, PlanGestionDechetsForm
from .ai_models import WasteManagementAI

# Create your views here.

# Vues pour TypeDechet
class TypeDechetListView(ListView):
    model = TypeDechet
    template_name = 'dechets/type_dechet_list.html'
    context_object_name = 'types_dechets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['biodegradable_count'] = TypeDechet.objects.filter(biodegradable=True).count()
        context['non_biodegradable_count'] = TypeDechet.objects.filter(biodegradable=False).count()
        return context

class TypeDechetDetailView(DetailView):
    model = TypeDechet
    template_name = 'dechets/type_dechet_detail.html'
    context_object_name = 'type_dechet'

class TypeDechetCreateView(SuccessMessageMixin, CreateView):
    model = TypeDechet
    form_class = TypeDechetForm
    template_name = 'dechets/type_dechet_form.html'
    success_url = reverse_lazy('dechets:type-dechet-list')
    success_message = "Type de déchet créé avec succès!"

class TypeDechetUpdateView(SuccessMessageMixin, UpdateView):
    model = TypeDechet
    form_class = TypeDechetForm
    template_name = 'dechets/type_dechet_form.html'
    success_message = "Type de déchet mis à jour avec succès!"
    
    def get_success_url(self):
        return reverse_lazy('dechets:type-dechet-detail', kwargs={'pk': self.object.pk})

class TypeDechetDeleteView(SuccessMessageMixin, DeleteView):
    model = TypeDechet
    template_name = 'dechets/type_dechet_confirm_delete.html'
    success_url = reverse_lazy('dechets:type-dechet-list')
    success_message = "Type de déchet supprimé avec succès!"

# Vues pour PlanGestionDechets
class PlanGestionDechetsListView(ListView):
    model = PlanGestionDechets
    template_name = 'dechets/plan_gestion_list.html'
    context_object_name = 'plans'

class PlanGestionDechetsCreateView(SuccessMessageMixin, CreateView):
    model = PlanGestionDechets
    form_class = PlanGestionDechetsForm
    template_name = 'dechets/plan_gestion_form.html'
    success_url = reverse_lazy('dechets:plan-list')
    success_message = "Plan de gestion créé avec succès!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            ai_model = WasteManagementAI()
            waste_type = self.request.POST.get('type_dechet')
            quantity = float(self.request.POST.get('quantite', 0))
            
            context['ai_recommendations'] = {
                'recommended_method': ai_model.recommend_treatment_method(
                    waste_type,
                    quantity,
                    self.get_biodegradable_status(waste_type)
                ),
                'predicted_efficiency': ai_model.predict_treatment_efficiency(
                    waste_type,
                    self.request.POST.get('methode_traitement'),
                    quantity,
                    self.get_current_conditions()
                )
            }
        return context

class PlanGestionDechetsUpdateView(SuccessMessageMixin, UpdateView):
    model = PlanGestionDechets
    form_class = PlanGestionDechetsForm
    template_name = 'dechets/plan_gestion_form.html'
    success_url = reverse_lazy('dechets:plan-list')
    success_message = "Plan de gestion mis à jour avec succès!"

class PlanGestionDechetsDeleteView(SuccessMessageMixin, DeleteView):
    model = PlanGestionDechets
    template_name = 'dechets/plan_gestion_confirm_delete.html'
    success_url = reverse_lazy('dechets:plan-list')
    success_message = "Plan de gestion supprimé avec succès!"

class PlanGestionDechetsDetailView(DetailView):
    model = PlanGestionDechets
    template_name = 'dechets/plan_gestion_detail.html'
    context_object_name = 'plan'
