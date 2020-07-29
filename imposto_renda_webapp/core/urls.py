from django.urls import path
from .views import ImpostoRendaView

urlpatterns = [
    path('calcular-imposto-renda', ImpostoRendaView.as_view())
]
