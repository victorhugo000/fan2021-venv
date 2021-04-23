from django.db import models

class Venda(models.Model):
    numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da venda')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=0)

    ProdutosE = models.ManyToManyField('Eletricos', blank=True, null=True, verbose_name ='Produtos Eletricos')
    Produtosh = models.ManyToManyField('Hidraulicos', blank=True, null=True, verbose_name ='Produtos hidraulicos')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Valor total da Venda')

    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    observacao = models.TextField(blank=True, null=True, verbose_name='Observação')
    comprovante_venda = models.FileField(blank=True, null=True, verbose_name='Comprovante de venda')
    venda_concluida = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return 'Comprador: ' + str(self.cliente) + ' | Data da venda: ' + str(self.data_venda)
class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='Email')

    def __str__(self):
        return str(self.nome)

class Eletricos(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.nome) + ' - R$: ' + str(self.valor)
class Hidraulicos(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.nome) + ' - R$: ' + str(self.valor)

class Vidros (models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    cor = models.CharField(max_length=255, blank=False, null=False)
    espessura = models.CharField(max_length=255, blank=True, null=True, verbose_name='Espessura')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.espessura) + ' - R$: ' + str(self.valor)
class Tintas (models.Model):
    cor = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    qtd_tintas = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Quantidade de tintas')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.cor) + '- R$: ' + str(self.valor)
class estrutura (models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)
class Pisos (models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)
class cobertas (models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    dimensaos = models.CharField(max_length=255, blank=False, null=False, verbose_name='Dimensões')
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)
class ferramentas (models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)


class iluminacao(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    ambiente = models.CharField(max_length=255, blank=False, null=False, verbose_name='Em qual ambiente será utilizada?')

    def __str__(self):
        return str(self.nome) + ' - R$: ' + str(self.valor)


