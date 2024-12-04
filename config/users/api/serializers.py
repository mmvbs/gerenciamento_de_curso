from rest_framework import serializers
from users.models import aluno
class alunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = aluno
        fields = '__all__'
    