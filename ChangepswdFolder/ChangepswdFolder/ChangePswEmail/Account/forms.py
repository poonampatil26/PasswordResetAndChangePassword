from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django import forms
from .models import Document


def validate_email(value):
    if User.objects.filter(email= value).exists():
        raise ValidationError((f'{value} is register already'), params={'value':value})

class UserForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)


        # def save(self, commit=True):
        #     user = super(UserForm, self).save(commit=False)
        #     user.email = self.cleaned_data.get("email")
        #     if commit:
        #         user.save()
        #     return user
        #
        # def clean_email(self):
        #     email = self.cleaned_data.get('email')
        #     if email and User.objects.filter(email=email).count() > 0:
        #         raise forms.ValidationError('This email address is already registered.')
        #     return email
        #
