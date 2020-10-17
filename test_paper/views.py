from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializerBeta
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class QuestionAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializerBeta(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializerBeta(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializerBeta(question)
        return Response(serializer.data)

    def put(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializerBeta(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def question_list(request):

    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializerBeta(questions, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = QuestionSerializerBeta(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', "PUT", "DELETE"])
def question_detail(request, pk):

    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = QuestionSerializerBeta(question)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuestionSerializerBeta(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
