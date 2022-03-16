from django.db import models
from django.urls import reverse

class Categories(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.CharField(max_length=255, verbose_name='URL')
    h1 = models.CharField(max_length=255, verbose_name='H1')
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.CharField(max_length=255, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('spravochnik:spravochnik-category-show', kwargs={'slug_category': self.slug})

    class Meta:
        verbose_name = 'Категория справочника'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Tags(models.Model):
    tag_name = models.CharField(max_length=255, verbose_name='Название тега')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    h1 = models.CharField(max_length=255, verbose_name='H1', null=True)
    title = models.CharField(max_length=255, verbose_name='Title', null=True)
    description = models.CharField(max_length=255, verbose_name='Description', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse('spravochnik:spravochnik-tag-show', kwargs={'slug_tag': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['tag_name']

class Spravochnik(models.Model):
    h1 = models.CharField(max_length=255, verbose_name='H1')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='Title')
    tags = models.ManyToManyField(Tags)
    description = models.CharField(max_length=255, verbose_name='Description')
    post_introduction = models.TextField(verbose_name='Вступление статьи')
    post = models.TextField(verbose_name='Статья')
    thumb_img_article = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Лого статьи')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT,
                                    verbose_name='Категория справочника')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at', 'title']

    def get_absolute_url(self):
        return reverse('spravochnik:spravochnik-article-show', kwargs={'slug_category': self.category.slug, 'slug_article': self.slug})

    def get_tags(self):
        # Получить все теги статьи
        return self.tags.all()
