# Generated by Django 4.0.3 on 2022-03-28 21:23

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bShop', '0002_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование товара')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('url', models.SlugField(max_length=266)),
                ('image', models.ImageField(upload_to='media/bShop/Item/%Y/%m/%d/', verbose_name='Главное фото')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='media/bShop/temp/shablon.jpg', upload_to='media/bShop/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='ReviewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bShop.item')),
            ],
        ),
        migrations.CreateModel(
            name='ImageItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media/bShop/Item/%Y/%m/%d/', verbose_name='Главное фото')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bShop.item')),
            ],
        ),
    ]
