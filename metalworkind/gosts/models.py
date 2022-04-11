from django.db import models
from django.urls import reverse

class GostSections(models.Model):
    section_number = models.CharField(max_length=7, unique=True, verbose_name='Номер раздела')
    section_name = models.CharField(max_length=255, unique=True, verbose_name='Название раздела')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    h1 = models.CharField(max_length=255, verbose_name='H1')
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.CharField(max_length=255, verbose_name='Description')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.section_number + ' ' + self.section_name

    def get_absolute_url(self):
        return reverse('gosts:gosts-section-show',
                       kwargs={'slug_gost_section': self.slug}
                       )

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['section_number']

class GostSubSections(models.Model):
    subsection_group = models.CharField(max_length=7, unique=True, verbose_name='Номер подраздела')
    subsection_name = models.CharField(max_length=255, verbose_name='Название подраздела')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    h1 = models.CharField(max_length=255, verbose_name='H1')
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.CharField(max_length=255, verbose_name='Description')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    section = models.ForeignKey(GostSections, on_delete=models.CASCADE,
                                    verbose_name='Раздел группы ГОСТа')

    def __str__(self):
        return self.subsection_group + ' ' + self.subsection_name

    def get_absolute_url(self):
        return reverse('gosts:gosts-group-show',
                       kwargs={'slug_gost_section': self.section.slug,
                               'slug_gost_group': self.slug}
                       )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['subsection_group']

class Gosts(models.Model):
    standard = models.CharField(max_length=255, verbose_name='Стандарт')
    standard_number = models.CharField(max_length=255, unique=True, verbose_name='Номер стандарта')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='Title')
    title_eng = models.CharField(max_length=255, blank=True, verbose_name='English title')
    h1 = models.CharField(max_length=255, verbose_name='H1')
    description = models.CharField(max_length=255, verbose_name='Description')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True)
    subsection = models.ForeignKey(GostSubSections, on_delete=models.CASCADE,
                                    verbose_name='Раздел подгруппы ГОСТа')

    def __str__(self):
        return self.standard + ' ' + self.standard_number

    def get_absolute_url(self):
        return reverse('gosts:gosts-article-show',
                       kwargs={'slug_gost_section': self.subsection.section.slug,
                               'slug_gost_group': self.subsection.slug,
                               'slug_gost': self.slug}
                       )

    class Meta:
        verbose_name = 'ГОСТ'
        verbose_name_plural = 'ГОСТы'
        ordering = ['standard_number']