from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from leads.models import Lead
from django.forms import *

User = get_user_model()


class LeadModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'age', 'agent')
        # labels = {
        #     'first_name': 'Nombres',
        #     'last_name': 'Apellidos',
        #     'age': 'Edad',
        #     'agent': 'Agente',
        # }
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre(s)',
                    'class': 'form-control',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese apellido(s)',
                    'class': 'form-control',
                }
            ),
            'age': NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'agent': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}
        widgets = {
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }