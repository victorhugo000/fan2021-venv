from django.db import models

class Venda(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome do produto')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Valor total da Venda')
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da venda')
    observacao = models.TextField(blank=True, null=True, verbose_name='Observação')
    comprovante_venda = models.FileField(blank=True, null=True, verbose_name='Comprovante de venda')
    exemplo_upload = models.FileField(upload_to='outro_diretorio/', null=True, blank=True)
    venda_concluida = models.BooleanField(blank=False, null=False)
    quantidade_itens = models.IntegerField(blank=True, null=False, verbose_name='Quantidade de Itens')
    produtos = models.ManyToManyField('Produto')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1)


    def _str_(self):
        return str(self.pk)+ '-' + self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    tipo = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def _str_(self):
        return self.nome + '. R$: ' + str(self.valor)


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='Email')


    def _str_(self):
        return self.nome