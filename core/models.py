from django.db import models

class Contato(models.Model):
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("Email")
    descricao = models.TextField("Descrição")
    data_envio = models.DateTimeField("Data de envio", auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"
