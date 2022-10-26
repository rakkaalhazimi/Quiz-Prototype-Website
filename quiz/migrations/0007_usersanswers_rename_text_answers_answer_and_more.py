# Generated by Django 4.1 on 2022-10-26 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("quiz", "0006_alter_scores_user_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="UsersAnswers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="answers",
            old_name="text",
            new_name="answer",
        ),
        migrations.RenameField(
            model_name="answers",
            old_name="option",
            new_name="choice",
        ),
        migrations.RenameField(
            model_name="answers",
            old_name="key_answer",
            new_name="is_right",
        ),
        migrations.RenameField(
            model_name="answers",
            old_name="question",
            new_name="question_id",
        ),
        migrations.RenameField(
            model_name="questions",
            old_name="serial",
            new_name="question_number",
        ),
        migrations.RemoveField(
            model_name="questions",
            name="text",
        ),
        migrations.AddField(
            model_name="questions",
            name="question",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Scores",
        ),
        migrations.AddField(
            model_name="usersanswers",
            name="answer_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="quiz.answers"
            ),
        ),
        migrations.AddField(
            model_name="usersanswers",
            name="question_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="quiz.questions"
            ),
        ),
        migrations.AddField(
            model_name="usersanswers",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
