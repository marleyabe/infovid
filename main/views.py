from django.shortcuts import render
from django.views import View
from main.models import Dados, Config
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError

# Create your views here.
class IndexView(View):
    def get(self, request):
        try:

            # dicionario que manda as informacoes do banco para a pagina
            data = {
                "dados" : Dados.objects.all(),
                "datahora" : timezone.localtime(Config.objects.get(pk=1).datahora_atualizacao)
            }

            return render(request, 'main/index.html', data)

        except Config.DoesNotExist:
            print('Dado Não existe')

            return render(request, 'main/atualizando.html', None)

        except OperationalError:
            print('db Não existe')

            return render(request, 'main/atualizando.html', None)



