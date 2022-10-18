from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    def check_password(self, password):
        return check_password(password, self.password_hash)

    @staticmethod
    def check_name(name):
        user = User.objects.filter(name=name)
        return len(user) > 0

    @staticmethod
    def check_username(username):
        user = User.objects.filter(username=username)
        return len(user) > 0

    @staticmethod
    def set_password(password):
        return make_password(password)


        

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