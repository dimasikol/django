# Generated by Django 4.0.3 on 2022-04-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bShop', '0006_remove_item_category_subcategory_item_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Кол=во'),
        ),
        migrations.AddField(
            model_name='item',
            name='keyitem',
            field=models.CharField(blank=True, default='0', max_length=1000, verbose_name='Код товара'),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, default=100, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='item',
            name='skidka',
            field=models.BooleanField(blank=True, default=False, verbose_name='Скида'),
        ),
    ]