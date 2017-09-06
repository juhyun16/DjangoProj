from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number=forms.CharField()
    address=forms.CharField()


    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields + ("email", )


    def save(self, commit=True):
        user=super().save()
        profile=Profile.objects.create(
            user=user, phone_number=self.cleaned_data["phone_number"],
            address=self.cleaned_data["address"]
        )
        return user


class LoginForm(AuthenticationForm):
    pass