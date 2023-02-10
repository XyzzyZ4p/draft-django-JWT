"""URL Configuration"""
from django.urls import path, include
# from .authentication import urls as auth_routes


urlpatterns = [
    path('', include('app.authentication.urls', namespace='app.authentication'))
]
