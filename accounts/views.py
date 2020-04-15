from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm


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

def edit_profile(request):

#  POST - save filled in form
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user).gi
        if form.is_valid:
            form.save()
            return redirect('/account/profile')
#  GET - load page initially
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


