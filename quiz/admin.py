from django.contrib import admin

from .models import Questions, Answers

# Register your models here.

# Create inline class to insert one model
# into another model form
class AnswersInline(admin.TabularInline):
    model = Answers

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("question_number", "question")
    ordering = ["question_number"]
    inlines = [
        AnswersInline,
    ]
    

admin.site.register(Questions, QuestionsAdmin)