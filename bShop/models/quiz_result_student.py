from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from picklefield.fields import PickledObjectField


class QuizResult(models.Model):
    answer = PickledObjectField()
    question_number = models.CharField(max_length=20)
    question_type = models.CharField(max_length=20)
    student = models.CharField(max_length=30)
    result = models.CharField(max_length=1000)
    quiz = PickledObjectField()
    date_create = models.DateTimeField(auto_now=True)
