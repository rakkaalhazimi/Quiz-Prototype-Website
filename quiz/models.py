from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
MAX_QUESTIONS = 10
ANSWER_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
)

class Questions(models.Model):
    question_number = models.IntegerField(
        default=1, 
        validators=[
            MaxValueValidator(MAX_QUESTIONS), 
            MinValueValidator(1)
        ])
    question = models.TextField()

    def __str__(self):
        return self.question
    

class Answers(models.Model):
    choice = models.CharField(max_length=1, choices=ANSWER_CHOICES)
    answer = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question_id} - {self.choice} - {self.answer}"


class UsersAnswers(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
