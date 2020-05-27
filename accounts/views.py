from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    # posts data from user to web server
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/account')
    # when there isn't data yet, GET request
    else:
        form = RegistrationForm()

        # create arg to refer to form through to template
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


def view_profile(request):
    # key: actual_data
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):

#  POST - save filled in form
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('/account/profile')
#  GET - load page initially
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)


        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/accounts/change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)