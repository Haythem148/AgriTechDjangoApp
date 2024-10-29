from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Avg, Sum
from django.utils import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import Pesticide, Application
from .forms import PesticideForm, ApplicationForm

# Create your views here.

class PesticideListView(ListView):
    model = Pesticide
    template_name = 'pesticides/pesticide_list.html'
    context_object_name = 'pesticides'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['herbicide_count'] = Pesticide.objects.filter(type_pesticide='herbicide').count()
        context['insecticide_count'] = Pesticide.objects.filter(type_pesticide='insecticide').count()
        context['fongicide_count'] = Pesticide.objects.filter(type_pesticide='fongicide').count()
        return context

class PesticideDetailView(DetailView):
    model = Pesticide
    template_name = 'pesticides/pesticide_detail.html'
    context_object_name = 'pesticide'

class PesticideCreateView(SuccessMessageMixin, CreateView):
    model = Pesticide
    form_class = PesticideForm
    template_name = 'pesticides/pesticide_form.html'
    success_url = reverse_lazy('pesticides:pesticide-list')
    success_message = "Pesticide créé avec succès!"

class PesticideUpdateView(SuccessMessageMixin, UpdateView):
    model = Pesticide
    form_class = PesticideForm
    template_name = 'pesticides/pesticide_form.html'
    success_message = "Pesticide mis à jour avec succès!"
    
    def get_success_url(self):
        return reverse_lazy('pesticides:pesticide-detail', kwargs={'pk': self.object.pk})

class PesticideDeleteView(SuccessMessageMixin, DeleteView):
    model = Pesticide
    template_name = 'pesticides/pesticide_confirm_delete.html'
    success_url = reverse_lazy('pesticides:pesticide-list')
    success_message = "Pesticide supprimé avec succès!"

# Application Views
class ApplicationListView(ListView):
    model = Application
    template_name = 'pesticides/application_list.html'
    context_object_name = 'applications'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate total applications
        context['total_applications'] = Application.objects.count()
        
        # Calculate total quantity
        total_quantity = Application.objects.aggregate(
            total=Sum('quantite'))['total']
        context['total_quantity'] = total_quantity or 0
        
        # Calculate applications this month
        today = timezone.now().date()
        first_day = today.replace(day=1)
        context['monthly_applications'] = Application.objects.filter(
            date_application__year=today.year,
            date_application__month=today.month
        ).count()
        
        return context

class ApplicationCreateView(SuccessMessageMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'pesticides/application_form.html'
    success_url = reverse_lazy('pesticides:application-list')
    success_message = "Application créée avec succès!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
           
            pesticide = self.request.POST.get('pesticide')
            quantity = float(self.request.POST.get('quantite', 0))
            
           
        return context

class ApplicationUpdateView(SuccessMessageMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'pesticides/application_form.html'
    success_url = reverse_lazy('pesticides:application-list')
    success_message = "Application mise à jour avec succès!"

class ApplicationDeleteView(SuccessMessageMixin, DeleteView):
    model = Application
    template_name = 'pesticides/application_confirm_delete.html'
    success_url = reverse_lazy('pesticides:application-list')
    success_message = "Application supprimée avec succès!"

class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'pesticides/application_detail.html'
    context_object_name = 'application'
