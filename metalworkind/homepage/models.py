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

class MetalPrices(models.Model):
    name = models.CharField(max_length=55, verbose_name='Название металла')
    chng_percents = models.FloatField(verbose_name='Изменение в %')
    chng_absolut = models.FloatField(verbose_name='Изменение абсолютное')
    unit = models.CharField(max_length=55, verbose_name='Единица измерения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цена на металл'
        verbose_name_plural = 'Цены на металлы'

class Currencies(models.Model):
    name = models.CharField(max_length=10, verbose_name='Код валюты')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Код валюты'
        verbose_name_plural = 'Коды валют'

class ExchangeRates(models.Model):
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE, verbose_name='Валюта')
    price = models.FloatField(verbose_name='Цена')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Новость')
    url = models.CharField(max_length=500, verbose_name='URL новости')
    source = models.CharField(max_length=55, verbose_name='Источник')
    published_date = models.DateField(verbose_name='Дата публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    def get_title_admin_panel(self):
        return self.title[:50] + ' ...'
    get_title_admin_panel.short_description = 'Заголовок новости'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
