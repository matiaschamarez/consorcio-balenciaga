"""
URL configuration for balenciaga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from applications.expensas.views import TotalSueldosView
from applications.gasto_administracion.views import GastoAdministracion
from applications.inicio.views import Home
from applications.login.views import Login



app_name = 'empleado'  # Reemplaza 'tu_aplicacion' con el nombre de tu aplicación


urlpatterns = [
    path('admin/', admin.site.urls),
    path('expensas/',TotalSueldosView.as_view(),name='expensas'),
    path('home/',Home.as_view(), name='home'),
    path('login/',Login.as_view(),name='login'),
]
