from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_Page, name='home'),
    path('about/', views.About_Page, name='about')
]
