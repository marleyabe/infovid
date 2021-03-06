from django.core.management.base import BaseCommand, CommandError
from main.models import Dados, Config
from utils.informacoes import pegar_informacoes
from django.utils import timezone


class Command(BaseCommand):

    def handle(self, *args, **options):
        # lista para organizar os dados para o banco de dados
        dados_data = []
        
        # Um loop para atualizar ou criar os dados dentro do banco de dados
        for i in range(27):
            dados = pegar_informacoes(i).split(";")

            dados_por_estado = "({0}, {1}, {2}, {3})".format(dados[0], dados[1], dados[2], dados[3])

            dado = Dados.objects.update_or_create(id=i+1,estado=dados[0], casos=dados[1], mortes=dados[2], novos_casos=dados[3])


        Config.objects.update_or_create(id=1, datahora_atualizacao=timezone.now())
