from django.urls import path, include
from django.conf import settings
from django.shortcuts import render, redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # runs before each view
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')

        if not request.user.is_authenticated():
            if True:
                return redirect(settings.LOGIN_URL)