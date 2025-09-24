from django.db import models

class Contato(models.Model):
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("Email")
    descricao = models.TextField("Descrição")
    data_envio = models.DateTimeField("Data de envio", auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"

class PlanoSaude(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=50)
    vantagens = models.TextField(help_text="Separe cada vantagem por ponto e vírgula (;)")

    CLASSES_CHOICES = [
        ('silver', 'Silver'),
        ('golden', 'Golden'),
    ]
    classe = models.CharField(max_length=20, choices=CLASSES_CHOICES, default='silver')

    def vantagens_lista(self):
        return self.vantagens.split(';')

    def __str__(self):
        return self.nome

class Vantagem(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição")
    icone_svg = models.TextField("Ícone SVG (código <svg>...</svg>)")

    def __str__(self):
        return self.titulo