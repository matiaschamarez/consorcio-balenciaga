from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def pagina_principal(request):
    return render(request, 'home/index.html')

class Home (TemplateView):
    template_name = 'home/index.html'
    
    