from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'status' ]

class EventoAddForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'status', 'data' ]


class EventFilterForm(forms.Form):
    search_query = forms.CharField(label='Buscar Eventos', required=False)
    