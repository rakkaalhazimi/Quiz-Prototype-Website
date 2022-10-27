from django.urls import path

from .views import IndexView, LeaderBoardView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("board", LeaderBoardView.as_view(), name="board"),
]