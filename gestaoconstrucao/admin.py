
from django.contrib import admin

from .models import Venda, Eletricos, Hidraulicos, Cliente, Vidros, Tintas, estrutura
from .models import Pisos, cobertas, ferramentas, iluminacao
# Register your models here.

admin.site.site_header = 'Gestão de construção'
admin.site.register(Venda)
admin.site.register(Eletricos)
admin.site.register(Cliente)
admin.site.register(Hidraulicos)
admin.site.register(Tintas)
admin.site.register(Vidros)
admin.site.register(estrutura)
admin.site.register(Pisos)
admin.site.register(cobertas)
admin.site.register(ferramentas)
admin.site.register(iluminacao)
