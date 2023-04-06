from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('api/v1/quotes', views.ExchangeRatesAPIVIEW.as_view()),
]