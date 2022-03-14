from django.db import models
from django.urls import reverse

class GostSections(models.Model):
    slug = models.CharField(max_length=255, verbose_name='URL')
    section_number = models.CharField(max_length=7, verbose_name='Номер раздела')
    section_name = models.CharField(max_length=255, verbose_name='Название раздела')
    h1 = models.CharField(max_length=255, verbose_name='H1')
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.CharField(max_length=255, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.section_number + ' ' + self.section_name

    class Meta:
        verbose_name = 'Раздел ГОСТов'
        verbose_name_plural = 'Разделы ГОСТов'
        ordering = ['section_number']

class GostSubSections(models.Model):
    slug = models.CharField(max_length=255, verbose_name='URL')
    subsection_group = models.CharField(max_length=7, verbose_name='Номер подраздела')
    subsection_name = models.CharField(max_length=255, verbose_name='Название подраздела')
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

    class Meta:
        verbose_name = 'Группа ГОСТов'
        verbose_name_plural = 'Группы ГОСТов'
        ordering = ['subsection_group']

class Gosts(models.Model):
    slug = models.CharField(max_length=255, verbose_name='URL')
    h1 = models.CharField(max_length=255, verbose_name='H1')
    title = models.CharField(max_length=255, verbose_name='Title')
    title_eng = models.CharField(max_length=255, verbose_name='Title')
    description = models.CharField(max_length=255, verbose_name='Description')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    standard = models.CharField(max_length=255, verbose_name='Стандарт')
    standard_number = models.CharField(max_length=255, verbose_name='Номер стандарта')
    subsection = models.ForeignKey(GostSubSections, on_delete=models.CASCADE,
                                    verbose_name='Раздел подгруппы ГОСТа')

    def __str__(self):
        return self.standard + ' ' + self.standard_number

    class Meta:
        verbose_name = 'ГОСТ'
        verbose_name_plural = 'ГОСТы'
        ordering = ['standard_number']