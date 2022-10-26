from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Questions(models.Model):
    max_questions = 10
    question_number = models.IntegerField(
        default=1, 
        validators=[
            MaxValueValidator(max_questions), 
            MinValueValidator(1)
        ])
    question = models.TextField()
    

class Answers(models.Model):
    options = ["A", "B", "C", "D"]
    option_choices = [(opt, opt) for opt in options]
    choice = models.CharField(max_length=1, choices=option_choices)
    answer = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)


class UsersAnswers(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
