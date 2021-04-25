
from django.contrib import admin

from .models import Venda, Eletricos, Hidraulicos, Cliente, Vidros, Tintas, Estrutura
from .models import Pisos, Cobertas, Ferramentas, Iluminacao, Esquadria, Madeira, Pedra, Maquina
# Register your models here.

admin.site.site_header = 'Gestão de construção'
admin.site.register(Venda)
admin.site.register(Eletricos)
admin.site.register(Cliente)
admin.site.register(Hidraulicos)
admin.site.register(Tintas)
admin.site.register(Vidros)
admin.site.register(Estrutura)
admin.site.register(Pisos)
admin.site.register(Cobertas)
admin.site.register(Ferramentas)
admin.site.register(Iluminacao)
admin.site.register(Esquadria)
admin.site.register(Madeira)
admin.site.register(Pedra)
admin.site.register(Maquina)
