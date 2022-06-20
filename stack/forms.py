from django.contrib.auth.models import User
from django import forms
from . models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio','email']