# Used for user signup form to extend UserCreationForm functionality but add email and first/lastname

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    firstName = forms.CharField(label='First Name', max_length=30)
    lastName = forms.CharField(label='Last Name', max_length=30)

    class Meta:
        model = User
        fields = ("username", "email", "firstName", "lastName")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["firstName"]
        user.last_name = self.cleaned_data["lastName"]
        if commit:
            user.save()
        return user