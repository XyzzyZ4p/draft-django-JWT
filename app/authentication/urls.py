from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView


app_name = 'app.authentication'

urlpatterns = [
    path('auth/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profile/', UserRetrieveUpdateAPIView.as_view())
]
