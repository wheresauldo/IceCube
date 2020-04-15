from django.shortcuts import redirect
from accounts import views

def login_redirect(request):
    return redirect('account/login')