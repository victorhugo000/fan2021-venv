
from django.contrib import admin

from .models import Venda, Eletricos, Hidraulico, Cliente, Vidro, Tinta, Esquadria, Madeira

# Register your models here.

admin.site.site_header = 'Gestão de construção'
admin.site.register(Venda)
admin.site.register(Eletricos)
admin.site.register(Cliente)
admin.site.register(Hidraulico)
admin.site.register(Vidro)
admin.site.register(Tinta)
admin.site.register(Esquadria)
admin.site.register(Madeira)