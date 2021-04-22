
from django.contrib import admin

from .models import Venda, Eletricos, Hidraulico, Cliente

# Register your models here.

admin.site.site_header = 'Gestão de construção'
admin.site.register(Venda)
admin.site.register(Eletricos)
admin.site.register(Cliente)
admin.site.register(Hidraulico)