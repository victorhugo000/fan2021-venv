from django.db import models

class Venda(models.Model):
    Produtos1 = models.ManyToManyField('Eletricos', verbose_name='Produtos Eletricos')
    Produtos2 = models.ManyToManyField('Hidraulico', verbose_name='Produtos hidraulicos')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Valor total da Venda')
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False, verbose_name='Número da venda')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1)
    observacao = models.TextField(blank=True, null=True, verbose_name='Observação')
    comprovante_venda = models.FileField(blank=True, null=True, verbose_name='Comprovante de venda')
    venda_concluida = models.BooleanField(blank=False, null=False)
    Produtosesq = models.ManyToManyField('Esquadria', blank=True, null=True)
    Produtosmad = models.ManyToManyField('Madeira', blank=True, null=True)
    Produtosmaq = models.ManyToManyField('Maquina', blank=True, null=True)
    Produtosped = models.ManyToManyField('Pedra', blank=True, null=True)


    def __str__(self):
        return str(self.cliente)


class Eletricos(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)

    def __str__(self):
        return self.nome + ' - R$: ' + str(self.valor)


class Hidraulico(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nome + '- R$: ' + str(self.valor)


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='Email')

    def __str__(self):
        return self.nome


class Vidro(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    cor = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.nome + '-R$: ' + str(self.valor)


class Tinta(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    cor = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.nome + '-R$: ' + str(self.valor)


class Esquadria(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    material = models.CharField(max_length=255, blank=False, null=False)
    cor = models.CharField(max_length=255, blank=False, null=False)
    dimencoes = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)


class Madeira(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    tipo = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    utiliz = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)


class Pedra(models.Model):
    tipo = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    utilizacao = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    cor = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return str(self.tipo) + '|' + str(self.utilizacao)


class Maquina(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    marca = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    cor = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.nome) + '|' + str(self.valor)