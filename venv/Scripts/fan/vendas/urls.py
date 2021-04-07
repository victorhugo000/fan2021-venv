from django.contrib import admin
from django.urls import path
from .views import VendaCreateview

urlpatterns = [
    path('cadastrar/venda', VendaCreateview.as_view(), name="cadastra_vendas"),

]
