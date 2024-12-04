from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.models import aluno
from users.api.serializers import alunoSerializer
from rest_framework.response import Response
from rest_framework import status

class alunoViewSet(ModelViewSet):
    serializer_class = alunoSerializer
    permission_classes = [AllowAny]
    queryset = aluno.objects.all()

    def criar_aluno(self, request):
        serializer = alunoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        novo_aluno = aluno.objects.create(
            nome=serializer.validated_data['nome'],
            matricula=serializer.validated_data['matricula'],
            user=serializer.validated_data['user']
        )

        serializer_saida = alunoSerializer(novo_aluno)
        return Response({"Info": "Cadatro realizado!", "data": serializer_saida.data}, status=status.HTTP_201_CREATED)