from django.urls import path
from .views import pagina_principal

urlpatterns = [
    path('pagina_principal/', pagina_principal),
]
