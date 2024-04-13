"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events.views import HomeView, EventoListView, EventoEditView, EventoDeleteView, EventoCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('lista_eventos/', EventoListView.as_view(), name='lista_eventos'),
    path('edit_eventos/<int:pk>/', EventoEditView.as_view(), name='edit_eventos'),
    path('del_evento/<int:pk>/', EventoDeleteView.as_view(), name='del_evento'),
    path('add_evento/', EventoCreateView.as_view(), name='add_evento'),
    path('account/', include('account.urls')),
]
