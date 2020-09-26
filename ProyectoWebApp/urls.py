from django.urls import path
from .views import *

urlpatterns = [
    path('home/',CategoriaListView.as_view(), name="CategoriasXFuncion"),
]