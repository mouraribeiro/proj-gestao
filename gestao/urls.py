
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('aplicativos.core.urls')),
    path('funcionarios,', include('aplicativos.funcionarios.urls')),
    path('empresa,', include('aplicativos.empresa.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
