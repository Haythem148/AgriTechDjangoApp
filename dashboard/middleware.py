from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs that don't require authentication
        exempt_urls = [
            reverse('dashboard:login'),
            reverse('dashboard:register'),
        ]

        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('dashboard:login')

        response = self.get_response(request)
        return response
