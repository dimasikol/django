# Generated by Django 4.0.3 on 2022-03-28 18:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Категория')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, default='media/bShop/templates/category.jpg', upload_to='media/bShop/Y%/m%/d%/', verbose_name='Изображение')),
                ('url', models.SlugField(max_length=1200, verbose_name='Ссылка')),
            ],
        ),
    ]
