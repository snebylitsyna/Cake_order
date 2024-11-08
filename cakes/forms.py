from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


class CityForm(forms.ModelForm):
    class Meta:
        model = models.City
        fields = ['name', 'country']
        widgets = {
            'name': forms.TextInput(),
            'country': forms.Select(),
        }


class ShopForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = ['name', 'city', 'adress']
        widgets = {
            'name': forms.TextInput(),
            'city': forms.Select(),
            'adress': forms.TextInput(),
        }


class GoodForm(forms.ModelForm):
    class Meta:
        model = models.Good
        fields = ['name', 'price', 'manufacturer', 'quantity', 'photo', 'status']
        widgets = {
            'name': forms.TextInput(),
            'price': forms.NumberInput(),
            'manufacturer': forms.Select(),
            'quantity': forms.NumberInput(),
            'photo': forms.FileInput(),
            'status': forms.Select(),
        }


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = models.Manufacturer
        fields = ['name']
        widgets = {
            'name': forms.TextInput(),
        }


class CreateUserForm(UserCreationForm):
    email = forms.CharField(
        label="E-mail",
        widget=forms.EmailInput(),
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user


class CakeForm(forms.ModelForm):
    class Meta:
        model = models.Cake
        fields = ['form', 'tier', 'filling', 'weight', 'photo', 'status','color', 'inscription', 'date_ready', 'shop',
                  'comments', 'client_name', 'phone_number']
        widgets = {
            'form': forms.Select(),
            'tier': forms.Select(),
            'filling': forms.Select(),
            'weight': forms.NumberInput(attrs={'step': 0.50, 'max': 4.00, "min": 1.00}),
            'status': forms.Select(),
            'photo': forms.FileInput(),
            'color': forms.TextInput(attrs={'type': 'color'}),
            'inscription': forms.TextInput(),
            'date_ready': forms.DateInput(attrs={'type': 'date'}),
            'shop': forms.Select(),
            'comments': forms.TextInput(),
            'client_name': forms.TextInput(),
            'phone_number': forms.TextInput(),
        }


class UpdateCakeForm(forms.ModelForm):
    class Meta:
        model = models.Cake
        fields = ['status']
        widgets = {
            'status': forms.Select(),
        }
