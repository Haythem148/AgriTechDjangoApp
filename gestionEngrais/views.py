from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.contrib import messages
from .models import Engrais, ApplicationEngrais
from .forms import EngraisForm, ApplicationEngraisForm

# List all Engrais
class EngraisListView(ListView):
    model = Engrais
    template_name = 'gestionEngrais/engrais_list.html'
    context_object_name = 'engrais'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_applications'] = ApplicationEngrais.objects.count()
        context['total_quantity'] = ApplicationEngrais.objects.aggregate(
            total=Sum('quantite'))['total'] or 0
        return context

# Add new fertilizer
class EngraisCreateView(SuccessMessageMixin, CreateView):
    model = Engrais
    form_class = EngraisForm
    template_name = 'gestionEngrais/engrais_form.html'
    success_url = reverse_lazy('gestionEngrais:engrais-list')
    success_message = "Fertilizer created successfully!"

class EngraisUpdateView(SuccessMessageMixin, UpdateView):
    model = Engrais
    form_class = EngraisForm
    template_name = 'gestionEngrais/engrais_form.html'
    success_url = reverse_lazy('gestionEngrais:engrais-list')
    success_message = "Fertilizer updated successfully!"

class EngraisDeleteView(SuccessMessageMixin, DeleteView):
    model = Engrais
    template_name = 'gestionEngrais/engrais_confirm_delete.html'
    success_url = reverse_lazy('gestionEngrais:engrais-list')
    success_message = "Fertilizer deleted successfully!"

# List all fertilizer applications
class ApplicationEngraisListView(ListView):
    model = ApplicationEngrais
    template_name = 'gestionEngrais/application_engrais_list.html'  # Changed from applicationengrais_list.html
    context_object_name = 'applications'
# Add new fertilizer application
class ApplicationEngraisCreateView(SuccessMessageMixin, CreateView):
    model = ApplicationEngrais
    form_class = ApplicationEngraisForm
    template_name = 'gestionEngrais/application_engrais_form.html'
    success_url = reverse_lazy('gestionEngrais:application-list')
    success_message = "Application created successfully!"

class ApplicationEngraisUpdateView(SuccessMessageMixin, UpdateView):
    model = ApplicationEngrais
    form_class = ApplicationEngraisForm
    template_name = 'gestionEngrais/application_engrais_form.html'
    success_url = reverse_lazy('gestionEngrais:application-list')
    success_message = "Application updated successfully!"

class ApplicationEngraisDeleteView(SuccessMessageMixin, DeleteView):  # Added SuccessMessageMixin
    model = ApplicationEngrais
    template_name = 'gestionEngrais/application_engrais_confirm_delete.html'  # Changed from applicationengrais_confirm_delete.html
    success_url = reverse_lazy('gestionEngrais:application-list')
    success_message = "Application deleted successfully!"

    def delete(self, request, *args, **kwargs):  # Add this method to show success message
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
