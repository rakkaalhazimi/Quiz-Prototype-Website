from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory

from .models import Answers


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = "__all__"
    

TestFormSet = formset_factory(AnswerForm, extra=len(Answers.options))
formset = TestFormSet()