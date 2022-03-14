# Generated by Django 4.0.2 on 2022-03-14 12:03

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
                ('category_name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.CharField(max_length=255, verbose_name='URL')),
                ('h1', models.CharField(max_length=255, verbose_name='H1')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Категория справочника',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255, verbose_name='Название тега')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('h1', models.CharField(max_length=255, null=True, verbose_name='H1')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['tag_name'],
            },
        ),
        migrations.CreateModel(
            name='Spravochnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=255, verbose_name='H1')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('post_introduction', models.TextField(verbose_name='Вступление статьи')),
                ('post', models.TextField(verbose_name='Статья')),
                ('thumb_img_article', models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Лого статьи')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликована')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='spravochnik.categories', verbose_name='Категория справочника')),
                ('tags', models.ManyToManyField(to='spravochnik.Tags')),
            ],
            options={
                'verbose_name': 'Справочник',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-created_at', 'title'],
            },
        ),
    ]
