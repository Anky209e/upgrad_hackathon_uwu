from django.urls import path,include
from . import views

urlpatterns = [
    path('fakenews/', views.fakenews,name='Fakenews')
]
