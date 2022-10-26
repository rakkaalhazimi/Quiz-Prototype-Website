from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import formset
from .models import Questions, Answers, UsersAnswers


# Create your views here.
class IndexView(generic.View):
    template_name = "index.html"

    @method_decorator(login_required(login_url="/login"), name="dispatch")
    def get(self, request):
        questions = Questions.objects.all()
        questions_answers = []
        for question in questions:
            questions_answers.append((question, Answers.objects.filter(question_id=question.id)))
        
        context = {"data": questions_answers}
        return render(request, self.template_name, context)

    def post(self, request):
        score = 0
        for question_id, choice in request.POST.items():
            if question_id == "csrfmiddlewaretoken":
                continue

            answer = Answers.objects.get(question_id=question_id, choice=choice)
            if answer.is_right:
                score += 5
        print(score)
        return redirect("board")


class LeaderBoardView(generic.View):
    template_name = "leader_board.html"

    def get(self, request):
        return render(request, self.template_name)

    def get_queryset(self):
        return self.model.objects.order_by("-score")