from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class QuizResult(models.Model):
    answer = models.CharField(max_length=1000)
    question_number = models.CharField(max_length=20)
    question_type = models.CharField(max_length=20)
    student = models.CharField(max_length=30)
    result = models.IntegerField()