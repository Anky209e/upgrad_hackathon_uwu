from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

landing = lambda request : redirect("/fakenews/")

urlpatterns = [
    path("",landing),
    path('admin/', admin.site.urls),
    path("fakenews/",include('fakenews.urls')),
]+static(settings.MEDIA_URL, doccument_root=settings.MEDIA_ROOT)
