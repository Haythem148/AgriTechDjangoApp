from django.shortcuts import render, redirect, get_object_or_404
from .models import SourceEau, UtilisationEau
from .forms import SourceEauForm, UtilisationEauForm
import json
import requests
from django.http import JsonResponse
from django.shortcuts import render


# List all water sources
def source_list(request):
    sources = SourceEau.objects.all()
    return render(request, 'water_management/source_list.html', {'sources': sources})

# Create a new water source
def source_create(request):
    if request.method == 'POST':
        form = SourceEauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('water_management:source_list')
    else:
        form = SourceEauForm()
    return render(request, 'water_management/source_form.html', {'form': form})

# Update a water source
def source_update(request, pk):
    source = get_object_or_404(SourceEau, pk=pk)
    if request.method == 'POST':
        form = SourceEauForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return redirect('water_management:source_list')
    else:
        form = SourceEauForm(instance=source)
    return render(request, 'water_management/source_form.html', {'form': form})

# Delete a water source
def source_delete(request, pk):
    source = get_object_or_404(SourceEau, pk=pk)
    if request.method == 'POST':
        source.delete()
        return redirect('water_management:source_list')
    return render(request, 'water_management/source_confirm_delete.html', {'source': source})

# Detail view for a water source
def source_detail(request, pk):
    source = get_object_or_404(SourceEau, pk=pk)
    return render(request, 'water_management/source_detail.html', {'source': source})


def utilisation_list(request):
    utilisations = UtilisationEau.objects.all()
    return render(request, 'water_management/utilisation_list.html', {'utilisations': utilisations})

def utilisation_create(request):
    form = UtilisationEauForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('water_management:utilisation_list')
    return render(request, 'water_management/utilisation_form.html', {'form': form})

def utilisation_update(request, pk):
    utilisation = get_object_or_404(UtilisationEau, pk=pk)
    form = UtilisationEauForm(request.POST or None, instance=utilisation)
    if form.is_valid():
        form.save()
        return redirect('water_management:utilisation_list')
    return render(request, 'water_management/utilisation_form.html', {'form': form})

def utilisation_delete(request, pk):
    utilisation = get_object_or_404(UtilisationEau, pk=pk)
    if request.method == 'POST':
        utilisation.delete()
        return redirect('water_management:utilisation_list')
    return render(request, 'water_management/utilisation_confirm_delete.html', {'utilisation': utilisation})

# Detail view for a water usage
def utilisation_detail(request, pk):
    utilisation = get_object_or_404(UtilisationEau, pk=pk)
    return render(request, 'water_management/utilisation_detail.html', {'utilisation': utilisation})

def get_water_prediction(request):
    if request.method == 'POST':
        api_url = "https://api-inference.huggingface.co/models/gpt2"  # Replace with your chosen model's URL
        api_key = "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"  # Replace with your API key

        # Parse the JSON body
        try:
            body = json.loads(request.body)
            input_text = body.get('input_text', 'What is the expected water quantity?')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "inputs": input_text,
        }

        # Call the Hugging Face API
        try:
            response = requests.post(api_url, headers=headers, json=data)
            response_data = response.json()

            if response.status_code == 200:
                return JsonResponse({'prediction': response_data})
            else:
                return JsonResponse({'error': 'API request failed', 'details': response_data}, status=response.status_code)

        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def water_prediction_view(request):
    return render(request, 'water_management/water_prediction.html')
