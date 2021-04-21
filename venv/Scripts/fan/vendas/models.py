from django.db import models

# Create your models here.

class vendas(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome da Venda')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,verbose_name='Valor da Venda')
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False,)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False,verbose_name='Nº do produto')
    observacao_venda = models.TimeField(blank=True, null=True, verbose_name='Observação')
    comprovante_venda = models.FileField(upload_to= 'comprovante_venda/',verbose_name='Comprovante da Venda')
    venda_concluida = models.BooleanField(blank=False, null=False,verbose_name='Venda concluída?')
    qtd_itens = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de itens')
    produtos = models.ManyToManyField('Produto')
    cliente = models.ForeignKey('Clientes', on_delete= models.DO_NOTHING, default=1)

    def __str__(self):
        return str(self.numero_venda) + ' - ' + self.nome


class Produto(models.Model):
    nome = models.CharField (max_length=255, blank=False, null=False, verbose_name='Nome do produto')
    quantidade = models.DecimalField(max_digits=16, decimal_places=2, null=False, blank=False, verbose_name='Quantidade de produtos')

    def __str__(self):
        return self.nome + ' - R$' + str(self.quantidade)


class Clientes (models.Model):
    nome = models.CharField (max_length=255, blank=False, null=False, verbose_name='Nome do cliente')
    CPF = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF do cliente')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='Email')

    def __str__(self):
        return self.nome

