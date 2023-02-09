"""URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from .simple import urls as simple_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(simple_urls))
]
