# Generated by Django 4.0.4 on 2022-05-01 13:56

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bShop', '0008_model_alter_item_sub_category_item_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_quiz', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(choices=[(1, '0'), (1, '1'), (1, '2'), (1, '3'), (1, '4'), (1, '5'), (1, '6'), (1, '7'), (1, '8'), (1, '9'), (1, '10'), (1, '11'), (1, '12'), (1, '13'), (1, '14'), (1, '15'), (1, '16'), (1, '17'), (1, '18'), (1, '19'), (1, '20'), (1, '21'), (1, '22'), (1, '23'), (1, '24'), (1, '25'), (1, '26')])),
            ],
        ),
        migrations.CreateModel(
            name='QuizType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(choices=[(1, 'oge'), (2, 'ege'), (3, 'diagnostic'), (4, 'create'), (5, None)])),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.IntegerField(unique=True)),
                ('student', models.CharField(max_length=30)),
                ('result', models.IntegerField()),
                ('question_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bShop.quizquestion')),
                ('question_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bShop.quiztype')),
            ],
        ),
        migrations.CreateModel(
            name='QuizCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('question', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bShop.quizcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bShop.quizcreate')),
            ],
        ),
    ]
