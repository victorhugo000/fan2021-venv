from django.shortcuts import render
from django.views.generic import CreateView
from .models import  vendas
from django.urls import reverse_lazy

# Create your views here.

class VendaCreateview(CreateView):
    model = vendas
    template_name = 'cadastrar/venda.html'
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("cadastra_vendas")
