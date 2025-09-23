from django.shortcuts import render
from .models import Contato

def index_view(request):
    contato = Contato.objects.first()
    mensagem = ""
    
    if request.method == "POST":
        mensagem = "Obrigado pelo contato!"

    return render(request, "core/index.html", {
        "contato": contato,
        "mensagem": mensagem
    })
