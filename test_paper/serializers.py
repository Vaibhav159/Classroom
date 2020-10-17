from test_paper.models import QUESTION_TYPES
from rest_framework import serializers
from .models import Question


class QuestionSerializerBeta(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'options']
