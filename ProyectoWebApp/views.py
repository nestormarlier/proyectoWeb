from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Categorias

# Create your views here.

def categoriasFunc(request):
   data = {
      'title': 'Listado categorías',
      'categorias': Categorias.objects.all()
   }
   return render(request,'dataTablexFuncion/list.html', data)


class CategoriaListView(ListView):
    model = Categorias
    template_name = "dataTablexFuncion/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Categorías'
        #context['object_list'] = Categorias.objects.filter(nombre__startswith = 'M') 
        context['object_list'] = Categorias.objects.all()
        return context
    


class eeCategoriaListView(ListView):
   model = Categorias
   template_name = 'dataTablexFuncion/list.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Listado de categorías'
       context['object_list'] = Categorias.objects.all()
       return context
   
   