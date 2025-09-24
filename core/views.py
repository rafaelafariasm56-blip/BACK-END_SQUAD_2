from django.shortcuts import render
from .models import Contato, PlanoSaude, Vantagem

def index_view(request):
    contato = Contato.objects.first()
    planos = PlanoSaude.objects.all()
    vantagens = Vantagem.objects.all()
    mensagem = ""

    if request.method == "POST":
        mensagem = "Obrigado pelo contato!"

    return render(request, "core/index.html", {
        "contato": contato,
        "planos": planos,
        "vantagens": vantagens,
        "mensagem": mensagem,
    })
