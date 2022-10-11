from django.urls import path,include
from . import views
from django.shortcuts import redirect

landing = lambda request : redirect("/fakenews/")

urlpatterns = [
    path("", landing),
    path("fakenews/",views.index),
    path("retrain/", views.retrain)
]
