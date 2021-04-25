
from django.contrib import admin

from .models import Venda, Eletricos, Hidraulico, Cliente, Vidro, Tinta, Esquadria, Madeira, Maquina, Pedra, Ceramica, Coberta, Piso, Estrutura, Iluminacao, Ferramenta

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
admin.site.register(Maquina)
admin.site.register(Pedra)
admin.site.register(Ceramica)
admin.site.register(Coberta)
admin.site.register(Piso)
admin.site.register(Estrutura)
admin.site.register(Iluminacao)
admin.site.register(Ferramenta)