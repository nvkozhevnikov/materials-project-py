# Generated by Django 4.0.2 on 2022-03-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marochnik', '0002_alter_categories_options_alter_materials_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='microstructures',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='microstructures',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликована'),
        ),
        migrations.AddField(
            model_name='microstructures',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='metal_color',
            field=models.IntegerField(verbose_name='Цвет металла'),
        ),
    ]