from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_View, name='contact')
]
