from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Категория')
    slug = models.CharField(max_length=255, unique=True, verbose_name='URL')
    metal_color = models.IntegerField(verbose_name='Цвет металла')
    h1 = models.CharField(max_length=255, verbose_name='H1', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Title', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Description', null=True, blank=True)
    post = models.TextField(verbose_name='Текст страницы', null=True, blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('marochnik:marochnik-subcategory-show', kwargs={'slug_category': self.slug})

    def count_materials(self):
        return Materials.objects.filter(subcategory__in=self.subcategories_set.all()).count()

class SubCategories(models.Model):
    name = models.CharField(max_length=255, unique=True,verbose_name='Подкатегория')
    slug = models.CharField(max_length=255, unique=True, verbose_name='URL')
    h1 = models.CharField(max_length=255, verbose_name='H1', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Title', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Description', null=True, blank=True)
    post = models.TextField(verbose_name='Текст страницы', null=True, blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('marochnik:marochnik-subcategory-show',
                       kwargs={'slug_category': self.slug}
                       )

    def get_absolute_url_one(self):
        return reverse('marochnik:marochnik-subcategory-one-show',
                       kwargs={'slug_category': self.category.slug,
                               'slug_subcategory': self.slug
                               }
                       )

class Materials(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Подкатегория')
    slug = models.CharField(max_length=255, unique=True, verbose_name='URL')
    h1 = models.CharField(max_length=255, verbose_name='H1', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Title', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Description', null=True, blank=True)
    main_properties = models.TextField(verbose_name='Характеристики', null=True, blank=True)
    him_sostav = models.TextField(verbose_name='Хим. состав', null=True, blank=True)
    meh_properties = models.TextField(verbose_name='Мех. свойства', null=True, blank=True)
    tehnol_properties = models.TextField(verbose_name='Технол. свойства', null=True, blank=True)
    fiz_properties = models.TextField(verbose_name='Физ. свойства', null=True, blank=True)
    tverdost = models.TextField(verbose_name='Твердость', null=True, blank=True)
    temp_krit_tchk = models.TextField(verbose_name='Темп. критич. точек', null=True, blank=True)
    vidy_postavki = models.TextField(verbose_name='Виды поставки', null=True, blank=True)
    inter_analogs = models.TextField(verbose_name='Зарубежные аналоги', null=True, blank=True)
    faq = models.TextField(verbose_name='FAQ', null=True, blank=True)
    sources = models.TextField(verbose_name='Источники данных', null=True, blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    subcategory = models.ForeignKey(SubCategories, on_delete=models.PROTECT, verbose_name='Подкатегория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('marochnik:marochnik-material-show',
                       kwargs={'slug_category': self.subcategory.category.slug,
                               'slug_subcategory': self.subcategory.slug,
                               'slug_material': self.slug
                               }
                       )

class Microstructures(models.Model):
    photo_href = models.CharField(max_length=255, unique=True, verbose_name='URL нахождения фото')
    photo_alt = models.CharField(max_length=255, verbose_name='Alt фото')
    photo_description = models.CharField(max_length=255, verbose_name='Описание фото', null=True, blank=True)
    material = models.ForeignKey(Materials, on_delete=models.PROTECT, verbose_name='Материал')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.photo_alt

    class Meta:
        verbose_name = 'Микроструктура'
        verbose_name_plural = 'Микроструктуры'
        ordering = ['pk']




