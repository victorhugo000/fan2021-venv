from django.contrib import admin
from .models import vendas, Produto, Clientes
# Register your models here.

admin.site.register(vendas)
admin.site.register(Produto)
admin.site.register(Clientes)