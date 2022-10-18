from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Questions(models.Model):
    MAX_QUESTION = 10
    serial = models.IntegerField(
        default=1, validators=[MaxValueValidator(MAX_QUESTION), MinValueValidator(1)])
    text = models.CharField(max_length=500)
    

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
    score = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)