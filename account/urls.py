from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('log-in/', auth_views.LoginView.as_view(), name='login'),
    path('log-out/', auth_views.LogoutView.as_view(), name='logout'),

]
