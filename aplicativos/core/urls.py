from django.urls import path

from aplicativos.core.views import home

urlpatterns = [
    path('', home),


]

