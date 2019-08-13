from django.shortcuts import redirect
from django.urls import path

from bandits_site.bandits_site import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('visualization/', views.visualization, name='visualization'),
    path('classic-ab-tests/', views.classic_ab_tests, name='classic_ab_tests'),
    path('multi-armed-bandits/', views.multi_armed_bandits, name='multi_armed_bandits'),
]