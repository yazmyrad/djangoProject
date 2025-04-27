from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class Registration(UserCreationForm):
    email = forms.EmailField(required=True)
    biotext = forms.CharField(max_length=150, required=False, widget=forms.Textarea)
    avatar  = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2" , "biotext", "avatar"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email field cannot be empty")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.cleaned_data.get('email'):
            raise ValueError("Email field cannot be empty")

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'bioText': self.cleaned_data.get('biotext', ''),
                    'avatar': self.cleaned_data.get('avatar')
                }
            )
            if not created:
                profile.bioText = self.cleaned_data.get('biotext', '')
                if self.cleaned_data.get('avatar'):
                    profile.avatar = self.cleaned_data['avatar']
                profile.save()
            
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)