from django.urls import path

from .views import EmpresaCreate

urlpatterns = [
    path('nova', EmpresaCreate.as_view(), name='create empresa'),


]

