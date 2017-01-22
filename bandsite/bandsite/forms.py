# Used for user signup form to extend UserCreationForm functionality but add email and first/lastname
# and create member object

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from bandmanager.models import Member, Band

class SignupForm(UserCreationForm):
    
    def getBands():
        bandList = []
        for eachBand in Band.objects.all():
            bandList.append((eachBand.pk, eachBand.name))
        return bandList
        
    email = forms.EmailField(label='Email', required=True)
    firstName = forms.CharField(label='First Name', max_length=30)
    lastName = forms.CharField(label='Last Name', max_length=30)
    band = forms.ChoiceField(widget=forms.Select, choices=getBands())

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
        # Create Member
        newBand = self.cleaned_data["band"]
        username = user.username
        pic = self.cleaned_data["picture"]
        member = Member(band=newBand, name=username, user=user, picture_url=pic, contact_info=user.email)
        member.save()
        return user