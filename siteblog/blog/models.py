from django.db import models

from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'категория(ю)'
        verbose_name_plural = 'категории'
        ordering = ['title']



class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тег')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Контент')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='posts')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-created_at']