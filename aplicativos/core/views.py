from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user

    return render(request, 'core/index.html', data)

