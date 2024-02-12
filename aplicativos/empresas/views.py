from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponse

from aplicativos.empresas.models import Empresa


# Create your views here.

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj =form.save()
        funcionario = self.request.user.funcionario
        funcionario.save()
        return HttpResponse('ok')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']