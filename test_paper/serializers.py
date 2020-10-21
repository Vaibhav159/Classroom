from test_paper.models import QUESTION_TYPES
from rest_framework import serializers
from .models import Question, Module


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'options', 'correct_ans']


"""class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'options', 'correct-answer']"""


class ModuleSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Module
        fields = ['id', 'moduleId', 'questions']

    def create(self, validated_data):
        question_data = validated_data.pop('questions')
        module = Module.objects.create(**validated_data)
        for question in question_data:
            qs = Question.objects.create(module=module, **question)
            module.questions.add(qs)
        return module
