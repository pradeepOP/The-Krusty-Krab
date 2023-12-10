from typing import Any
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["body"]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
     
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self.add_error('password1', 'Passwords didnot match')


