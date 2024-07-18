from django import forms
from .models import Cidade

# Define o formulário CidadeForm baseado no modelo Cidade.
class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome']
