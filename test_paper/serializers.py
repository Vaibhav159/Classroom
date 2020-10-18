from test_paper.models import QUESTION_TYPES
from rest_framework import serializers
from .models import Question, Module


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'options']


"""class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'options', 'correct-answer']"""


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['moduleId', 'questions']
