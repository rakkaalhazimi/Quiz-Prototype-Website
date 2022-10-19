from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Questions(models.Model):
    MAX_QUESTION = 10
    serial = models.IntegerField(
        default=1, 
        validators=[MaxValueValidator(MAX_QUESTION), MinValueValidator(1)])
    text = models.CharField(max_length=500)

    def get_answers(self):
        return Answers.objects.filter(question=self.id)

    @classmethod
    def get_questions(cls):
        return cls.objects.all()

    @classmethod
    def get_questions_answers(cls):
        for question in cls.get_questions():
            yield question, question.get_answers()
    

class Answers(models.Model):
    class Options(models.TextChoices):
        A = "A"
        B = "B"
        C = "C"
        D = "D"

    option = models.CharField(max_length=1, choices=Options.choices)
    text = models.CharField(max_length=255)
    key_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)


class Scores(models.Model):
    POINT = 5
    score = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @classmethod
    def create_or_get_score(cls, user):
        if not cls.objects.filter(user=user):
            score = cls(user=user, score=0)
            score.save()
            return score
        return cls.objects.get(user=user)

    def set_score(self, question_ids, options):
        score = 0
        
        for question_id, option in zip(question_ids, options):
            if question_id == "csrfmiddlewaretoken":
                continue
            answer = Answers.objects.get(question=question_id, option=option)
            if answer.key_answer:
                score += self.POINT
        
        self.score = score
        self.save()
        
            
        