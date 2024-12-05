import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from cursos.models import curso
from cursos.api.serializers import cursoSerializer, inscricaoSerializer
from rest_framework.viewsets import ModelViewSet
from cursos.models import curso, inscricao

logger = logging.getLogger("cursos")
class cursoViewSet(ModelViewSet):
    cursoSerializer = cursoSerializer
    permission_classes = [AllowAny]
    queryset = curso.objects.all()

    def create(self, request):
        serializer = cursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        nome = serializer.validated_data['nome']
        categoria = serializer.validated_data['categoria']

        in_database = curso.objects.filter(nome=nome, categoria=categoria).exists()

        if not in_database:
            novo_curso = curso.objects.create(
                nome=serializer.validated_data['nome'],
                vagas=serializer.validated_data['vagas'],
                titulo=serializer.validated_data['titulo'],
                descricao=serializer.validated_data['descricao'],
                categoria=serializer.validated_data['categoria'],
                conteudo=serializer.validated_data['conteudo']
            )

            serializer_saida = cursoSerializer(novo_curso)
            logger.info("Curso cadastrado com sucesso!")
            return Response({"Info": "Curso cadastrado!", "data": serializer_saida.data}, status=status.HTTP_201_CREATED)
        else:
            logger.error("curso já cadastrado!")
            return Response({"Info": "Falha ao tentar cadastrar o curso!"}, status=status.HTTP_409_CONFLICT)
    
    #from rest_framework.decorators import action
    #http://localhost:8000/cursos/buscar/
    #@action(methods=['get'],detail=False,url_path="buscar")
    def buscar_cursos(self, request):
        busca = curso.objects.all()
        serializer = cursoSerializer(busca, many=True)
        return Response({"Info":"Lista de cursos", "data":serializer.data}, status=status.HTTP_200_OK)
    
class inscricaoViewSet(ModelViewSet):
    inscricaoSerializer = inscricaoSerializer
    permission_classes = [IsAuthenticated]
    queryset = inscricao.objects.all()

    def create(self, request):
        serializer = inscricaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        aluno = serializer.validated_data['aluno']
        curso = serializer.validated_data['curso']

        in_database = inscricao.objects.filter(aluno=aluno, curso=curso).exists()

        if not in_database:
            nova_inscricao = inscricao.objects.create(
                aluno=serializer.validated_data['aluno'],
                curso=serializer.validated_data['curso']
            )

            serializer_saida = inscricaoSerializer(nova_inscricao)
            logger.info("Inscrição realizada com sucesso!")
            return Response({"Info": "Inscrição realizada!", "data": serializer_saida.data}, status=status.HTTP_201_CREATED)
        else:
            logger.error("Inscrição já realizada!")
            return Response({"Info": "Falha ao tentar realizar a inscrição!"}, status=status.HTTP_409_CONFLICT)
    
