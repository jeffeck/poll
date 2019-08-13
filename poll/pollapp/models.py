from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)


class Question(models.Model):
    def __str__(self):
        return str(self.id) + ": " + self.text

    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=100)
    question_type = models.TextField(max_length=15)


class Answers(models.Model):
    def __str__(self):
        return str(self.id) + ": " + self.description

    class Meta:
        verbose_name_plural = "Answers"

    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)


class Responses(models.Model):
    class Meta:
        verbose_name_plural = "Responses"

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True)
    answers = models.ManyToManyField(Answers)
