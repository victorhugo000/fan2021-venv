
from django.contrib import admin

from .models import Venda, Produto, Cliente

# Register your models here.

admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Cliente)
