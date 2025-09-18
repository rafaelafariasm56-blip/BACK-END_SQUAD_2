from django.db import models
import os
import sys
import os
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animaliscare.settings')
django.setup()

from blog.models import MeuModelo

for obj in MeuModelo.objects.all():
    print(obj)

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
