from django.db import models

class About(models.Model):
    h1 = models.CharField(max_length=255, verbose_name='H1')
    slug = models.CharField(max_length=255, unique=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='Title')
    breadcrumb_text = models.CharField(max_length=255, verbose_name='Текст хлебной крошки')
    post = models.TextField(verbose_name='Текст страницы')
    description = models.CharField(max_length=255, verbose_name='Description')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.h1

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
