from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Rubric(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rubric', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'рубрика(у)'
        verbose_name_plural = 'рубрики'
        ordering = ['name']


class Article(models.Model):
    name = models.CharField(max_length=255)
    category = TreeForeignKey(Rubric, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'статья(ю)'
        verbose_name_plural = 'статьи'
        ordering = ['name']