from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum, IntegerField, Value
from django.db.models.functions import Concat
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import generic

from .models import Questions, Answers, UsersAnswers


# Create your views here.
class IndexView(generic.View):
    template_name = "index.html"

    @method_decorator(login_required(login_url="/login"), name="dispatch")
    def get(self, request):
        questions = Questions.objects.all()
        questions_answers = []
        
        for question in questions:
            answers = Answers.objects.filter(question=question.id)
            questions_answers.append((question, answers))
        
        context = {"data": questions_answers}
        return render(request, self.template_name, context)

    def post(self, request):
        for question_id, answer_id in request.POST.items():
            if question_id == "csrfmiddlewaretoken":
                continue

            question = Questions.objects.get(id=question_id)
            answer = Answers.objects.get(id=answer_id, question=question_id)

            try:
                user_answer = UsersAnswers.objects.get(user=request.user, question=question)
                user_answer.answer = answer
                user_answer.save()

            except UsersAnswers.DoesNotExist:
                user_answer = UsersAnswers(user=request.user, question=question, answer=answer)
                user_answer.save()

        return redirect("board")


class LeaderBoardView(generic.ListView):
    model = UsersAnswers
    template_name = "leader_board.html"

    def get_queryset(self):
        # Group all user by its score
        # Score is a total of correct answers multiplied by some constant
        full_name = Concat(F("user__first_name"), Value(" "), F("user__last_name"))
        score = Sum("answer__is_right", output_field=IntegerField()) * 5
        
        return (self.model.objects.values("user__first_name")
                                  .annotate(name=full_name)
                                  .annotate(score=score)
                                  .order_by("score"))