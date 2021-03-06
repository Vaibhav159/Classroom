from django.urls import path
from .views import QuestionAPIView, QuestionDetailView, ModuleAPIView, ModuleDetailView

urlpatterns = [
    #path("question/", question_list),
    path("question/", QuestionAPIView.as_view()),
    #path('detail/<int:pk>', question_detail)
    path('detail/<int:pk>', QuestionDetailView.as_view()),
    path('module/', ModuleAPIView.as_view()),
    path('details/<int:pk>', ModuleDetailView.as_view()),
]
