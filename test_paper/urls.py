from django.urls import path
from .views import question_list, question_detail, QuestionAPIView, QuestionDetailView

urlpatterns = [
    #path("question/", question_list),
    path("question/", QuestionAPIView.as_view()),
    #path('detail/<int:pk>', question_detail)
    path('detail/<int:pk>', QuestionDetailView.as_view())
]
