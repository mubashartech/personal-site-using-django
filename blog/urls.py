from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_Home, name='blog-home'),
    path('<int:id>/', views.blog_Detail, name='blog-detail')
]
