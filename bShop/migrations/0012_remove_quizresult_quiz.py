# Generated by Django 4.0.4 on 2022-05-02 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bShop', '0011_quizresult_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='quiz',
        ),
    ]