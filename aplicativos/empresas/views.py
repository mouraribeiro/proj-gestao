from django.shortcuts import render
from django.views.generic import CreateView

from aplicativos.empresas.models import Empresa


# Create your views here.

class EmpresaCreate(CreateView):
    model = Empresa