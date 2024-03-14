from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GabrielNode
from .serializers import GabrielNodeSerializer

# Create your views here.
class NodeData(APIView):
    def post(self, request):
        data = request.data
        gabriel_node = GabrielNodeSerializer(
            data={
                "sensor": data["Sensor"],
                "botao": data["Botao"],
                "liga_robo": data["LigaRobo"],
                "reset_contador": data["ResetContador"],
                "valor_contagem": data["Valor Contagem"],
            }
        )
        gabriel_node.is_valid(raise_exception=True)
        gabriel_node.save()
        return Response(gabriel_node.data)

    def get(self, request):
        atividade = GabrielNode.objects.latest('id')
        # Renderizando o template HTML e passando os dados das atividades
        return render(request, 'node.html', {'atividade': atividade})

