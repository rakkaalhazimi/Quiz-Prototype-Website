from django.urls import path

from .views import IndexView, LeaderBoardView, test_view

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("board", LeaderBoardView.as_view(), name="board"),
    path("test", test_view, name="test"),
]