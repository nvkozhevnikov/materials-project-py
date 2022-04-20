# Generated by Django 4.0.2 on 2022-03-30 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Категория')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='URL')),
                ('metal_color', models.IntegerField(max_length=3, verbose_name='Цвет металла')),
                ('h1', models.CharField(blank=True, max_length=255, null=True, verbose_name='H1')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('post', models.TextField(blank=True, null=True, verbose_name='Текст страницы')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликована')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Подкатегория')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='URL')),
                ('h1', models.CharField(blank=True, max_length=255, null=True, verbose_name='H1')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('post', models.TextField(blank=True, null=True, verbose_name='Текст страницы')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликована')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marochnik.categories', verbose_name='Категория марочника')),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Подкатегория')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='URL')),
                ('h1', models.CharField(blank=True, max_length=255, null=True, verbose_name='H1')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('main_properties', models.TextField(blank=True, null=True, verbose_name='Характеристики')),
                ('him_sostav', models.TextField(blank=True, null=True, verbose_name='Хим. состав')),
                ('meh_properties', models.TextField(blank=True, null=True, verbose_name='Мех. свойства')),
                ('tehnol_properties', models.TextField(blank=True, null=True, verbose_name='Технол. свойства')),
                ('fiz_properties', models.TextField(blank=True, null=True, verbose_name='Физ. свойства')),
                ('tverdost', models.TextField(blank=True, null=True, verbose_name='Твердость')),
                ('temp_krit_tchk', models.TextField(blank=True, null=True, verbose_name='Темп. критич. точек')),
                ('vidy_postavki', models.TextField(blank=True, null=True, verbose_name='Виды поставки')),
                ('inter_analogs', models.TextField(blank=True, null=True, verbose_name='Зарубежные аналоги')),
                ('faq', models.TextField(blank=True, null=True, verbose_name='FAQ')),
                ('sources', models.TextField(blank=True, null=True, verbose_name='Источники данных')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликована')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marochnik.subcategories', verbose_name='Подкатегория марочника')),
            ],
        ),
    ]
