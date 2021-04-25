from django.db import models

#Deverão ser criadas pelo menos 15 classes contendo um mínimo de:
#- 2 classes com pelo menos 10 atributos(Venda,);
#- 3 classes com pelo menos 7 atributos(esquadrias);
#- 5 classes com pelo menos 5 atributos(Vidros,tintas, cobertas, ferramentas,iluminacao);
#- 5 classes com pelo menos 3 atributos(Cliente, eletricos, hidraulicos, estrutura, pisos).


class Venda(models.Model):
    numero_venda = models.IntegerField(blank=False, null=True, verbose_name='Número da venda')
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=0)

    ProdutosEletricos = models.ManyToManyField('Eletricos', blank=True, null=True, verbose_name='Estoque: Eletricos')
    Produtoshi = models.ManyToManyField('Hidraulicos', blank=True, null=True, verbose_name='Estoque:hidraulicos')
    Produtosvidros = models.ManyToManyField('Vidros', blank=True, null=True, verbose_name='Estoque: Vidros')
    ProdutosTintas = models.ManyToManyField('Tintas', blank=True, null=True, verbose_name='Estoque: Tintas')
    ProdutosEstrutura = models.ManyToManyField('estrutura', blank=True, null=True, verbose_name='Estoque: Estrutura')
    ProdutosPisos = models.ManyToManyField('Pisos', blank=True, null=True, verbose_name='Estoque: Pisos')
    ProdutosCobertas = models.ManyToManyField('cobertas', blank=True, null=True, verbose_name='Estoque: Cobertas')
    Produtosfer = models.ManyToManyField('ferramentas', blank=True, null=True, verbose_name='Estoque: Ferramentas')
    Produtosiluminacao = models.ManyToManyField('iluminacao', blank=True, null=True, verbose_name='Estoque: iluminacao')
    Produtosesq = models.ManyToManyField('Esquadria', blank=True, null=True, verbose_name='Estoque: Esquadrias')
    Produtosmad = models.ManyToManyField('Madeira', blank=True, null=True, verbose_name='Estoque: Madeira')
    Produtosmaq = models.ManyToManyField('Maquina', blank=True, null=True, verbose_name='Estoque: Maquina')
    Produtosped = models.ManyToManyField('Pedra', blank=True, null=True, verbose_name='Estoque: Pedra')

    valor = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=False,
                                verbose_name='Valor total da Venda')

    data_venda = models.DateField(auto_now_add=True, blank=True, null=True)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=True)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True, verbose_name='Observação')
    comprovante_venda = models.FileField(blank=True, null=True, verbose_name='Comprovante de venda')
    venda_concluida = models.BooleanField(blank=False, null=True)

    def __str__(self):
        return 'Comprador: ' + str(self.cliente) + ' | Data da venda: ' + str(self.data_venda)


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0, verbose_name='Nome')
    cpf = models.CharField(max_length=11, blank=False, null=True, default=0, verbose_name='CPF')
    email_cliente = models.EmailField(blank=True, null=True, verbose_name='Email')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome)


class Eletricos(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + ' - R$: ' + str(self.valor)


class Hidraulicos(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + ' - R$: ' + str(self.valor)


class Vidros(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    cor = models.CharField(max_length=255, blank=False, null=False)
    espessura = models.CharField(max_length=255, blank=True, null=True, default=0, verbose_name='Espessura')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.espessura) + ' - R$: ' + str(self.valor)


class Tintas(models.Model):
    cor = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    qtd_tintas = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                     verbose_name='Quantidade de tintas')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.cor) + '- R$: ' + str(self.valor)


class Estrutura(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)


class Pisos(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)


class Cobertas(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    dimensaos = models.CharField(max_length=255, blank=False, null=True, default=0, verbose_name='Dimensões')
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)


class Ferramentas(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')
    jogo = models.BooleanField(blank=True, null=True, verbose_name='Jogo de ferramentas')
    individual = models.BooleanField(blank=True, null=True, verbose_name='Individual')

    def __str__(self):
        return str(self.nome) + '- R$: ' + str(self.valor)


class Iluminacao(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    ambien = models.CharField(max_length=255, blank=False, null=True, default=0, verbose_name='Em qual ambiente será utilizada?')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + ' - R$: ' + str(self.valor)


class Esquadria(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    material = models.CharField(max_length=255, blank=False, null=True, default=0, verbose_name='Material')
    cor = models.CharField(max_length=255, blank=False, null=True, default=0)
    dim = models.CharField(max_length=255, blank=False, null=True, default=0, verbose_name='Dimensões:')
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    des = models.TextField(blank=True, null=True, verbose_name='Descrição:')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + ' - R$: ' + str(self.valor)


class Madeira(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    tipo = models.CharField(max_length=255, blank=False, null=True, default=0)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    utiliz = models.CharField(max_length=255, blank=False, null=True, default=0, verbose_name='Qual a utilização?')
    metros = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    formato = models.CharField(max_length=255, blank=False, null=True, default=0)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + ' - R$: ' + str(self.valor)


class Pedra(models.Model):
    tipo = models.CharField(max_length=255, blank=False, null=True, default=0)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    utilizacao = models.CharField(max_length=255, blank=False, null=True, default=0, verbose_name='Onde será utilizado?')
    descricao = models.TextField(blank=True, null=True, verbose_name='descrição')
    cor = models.CharField(max_length=255, blank=False, null=True)
    metros = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    formato = models.CharField(max_length=255, blank=False, null=True, default=0)
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.tipo) + '  |  ' + str(self.utilizacao)


class Maquina(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, default=0)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    descricao = models.TextField(blank=True, null=True, verbose_name='descrição')
    nomeCondutor = models.CharField(max_length=255, blank=True, null=True, default=0, verbose_name='Nome do condutor')
    cpfCondutor = models.CharField(max_length=11, blank=True, null=True, default=0, verbose_name='CPF do condutor')
    cnhCondutor = models.CharField(max_length=10, blank=True, null=True, default=0, verbose_name='CPF')
    placa = models.CharField(max_length=255, blank=True, null=True, default=0, verbose_name='Placa')
    Marca = models.CharField(max_length=255, blank=True, null=True, default=0, verbose_name='Marca')
    Cor = models.CharField(max_length=255, blank=True, null=True, default=0, verbose_name='Cor')
    confirmacao = models.BooleanField(blank=False, null=False, verbose_name='Confirmar cadastro')

    def __str__(self):
        return str(self.nome) + '  |  ' + str(self.valor)