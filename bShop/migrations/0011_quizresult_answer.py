# Generated by Django 4.0.4 on 2022-05-02 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bShop', '0010_alter_quizquestion_name_alter_quiztype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresult',
            name='answer',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]