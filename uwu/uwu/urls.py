from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    path("",include("fakenews.urls")),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, doccument_root=settings.MEDIA_ROOT)
