from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.models import aluno, Professor
from users.api.serializers import alunoSerializer, ProfessorSerializer, ProfessorCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group

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
        return Response({"Info": "Cadatro do aluno realizado!", "data": serializer_saida.data}, status=status.HTTP_201_CREATED)
    
class ProfessorViewSet(ModelViewSet):
    serializer_class = ProfessorSerializer
    permission_classes = [AllowAny]
    queryset = Professor.objects.all()

    def criar_Professor(self, request):
        serializer = ProfessorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        novo_user = Professor.objects.create_user(
            username=serializer.validated_data['login'],
            password=serializer.validated_data['senha'],
        )
        grupo_professores = Group.objects.get(name="Professores")
        novo_user.groups.add(grupo_professores)

        novo_professor = Professor.objects.create(
            nome=serializer.validated_data['nome'],
            matricula=serializer.validated_data['matricula'],
            curso=serializer.validated_data['curso'],
            user=novo_user
        )

        serializer_saida = ProfessorSerializer(novo_professor)
        return Response({"Info": "Cadastro do professor realizado!", "data":serializer_saida.data}, status=status.HTTP_201_CREATED)