# Generated by Django 4.0.4 on 2022-05-02 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bShop', '0012_remove_quizresult_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='quiztype',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
