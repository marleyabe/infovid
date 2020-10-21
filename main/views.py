from django.shortcuts import render
from django.views import View
from main.models import Dados
# Create your views here.
class IndexView(View):
    def get(self, request):

        # dicionario que manda as informacoes do banco para a pagina
        data = {
            "dados" : Dados.objects.all()    
        }

        return render(request, 'main/index.html', data)