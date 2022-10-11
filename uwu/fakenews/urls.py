from django.urls import path,include
from . import views

landing = lambda request : redirect("/fakenews/")

urlpatterns = [
    path("", landing),
    path("fakenews/",views.index),
    path("retrain/", views.retrain)
]
