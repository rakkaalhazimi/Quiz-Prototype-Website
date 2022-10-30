from django.urls import path

from .views import IndexView, LeaderBoardView, QuizResultView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("board", LeaderBoardView.as_view(), name="board"),
    path("result", QuizResultView.as_view(), name="result"),
]