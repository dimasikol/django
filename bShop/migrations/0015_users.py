# Generated by Django 4.0.4 on 2022-05-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bShop', '0014_alter_quizresult_question_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_register', models.DateField(auto_created=True)),
                ('login', models.CharField(max_length=40, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('second_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='media/users/%Y/%m/%d/')),
                ('about', models.TextField(blank=True)),
                ('password', models.CharField(max_length=50)),
                ('date_enter', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
