from django import forms
from django.contrib.auth import get_user_model
from .models import Reviews
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class ReviewsForm(forms.ModelForm):
    rate = forms.Widget(attrs={'type': "hidden"})
    class Meta:
        model = Reviews
        fields = ['title', 'name', 'comment', 'rate']
        # rate = forms.CharField(widget=forms.HiddenInput())
        widgets = {'rate': forms.HiddenInput(),
                   'title': forms.TextInput(attrs={"class": 'form-control'}),
                   'name': forms.TextInput(attrs={"class": 'form-control'}),
                   'comment': forms.Textarea(attrs={"class": 'form-control'})}


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class UserSignupForm(UserCreationForm):
#     password1 = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label=_("Password confirmation"),
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#         strip=False,
#         help_text=_("Enter the same password as before, for verification."),
#     )

#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {'username': UsernameField}