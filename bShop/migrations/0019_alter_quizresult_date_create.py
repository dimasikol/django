# Generated by Django 4.0.4 on 2022-05-10 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bShop', '0018_quizresult_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresult',
            name='date_create',
            field=models.DateTimeField(auto_now=True),
        ),
    ]