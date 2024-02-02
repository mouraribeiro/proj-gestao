from django.urls import path, include

from aplicativos.funcionarios.views import home

urlpatterns = [
    path('', home),


]

