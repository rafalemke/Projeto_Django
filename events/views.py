from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from .forms import EventoForm, EventoAddForm, EventFilterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests


# Create your views here.

class HomeView(TemplateView):
    
    template_name = 'events/home.html'
    

@method_decorator(login_required, name='dispatch')
class EventoListView(ListView):
    model = Evento
    template_name = 'events/lista_eventos.html'
    context_object_name = 'eventos'
    form_class = EventFilterForm

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')

        if status:
            queryset = queryset.filter(status=status)

        return queryset

@method_decorator(login_required, name='dispatch')
class EventoEditView(UpdateView):
    model = Evento
    template_name = 'events/edit_eventos.html'
    context_object_name = 'eventos'
    form_class = EventoForm
    success_url = reverse_lazy('lista_eventos')
    def form_valid(self, form):
        
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'events/del_evento.html'
    success_url = reverse_lazy('lista_eventos')
    

@method_decorator(login_required, name='dispatch')
class EventoCreateView(CreateView):
    model = Evento
    template_name = 'events/add_evento.html'
    context_object_name = 'eventos'
    form_class = EventoAddForm
    success_url = reverse_lazy('lista_eventos')



def get_weather_data(ip_address):
    api_key = "YOUR_WEATHERAPI_KEY"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={ip_address}"
    response = requests.get(url)
    data = response.json()
    return data

