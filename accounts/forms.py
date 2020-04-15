from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

   # define the meta data that relates to this class I'm side of
    # analogy: class == photo, meta class == resolution of the photo
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

# create method to save data to model

        def save(self,commit=True):
            # super gains access to inherited methods from a parent or sib class
            # commit = False bc its there isn't date entered yet to POST to data base

            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

# if cleaned_Data provided, save in database using sql

            if commit:
                user.save()

            return user

class EditProfileForm(UserChangeForm):
# exclude or fields
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'

        )

