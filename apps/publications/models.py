from django.db import models


class PublicationCategory(models.Model):
    """Модель для категории публикации"""
    title = models.CharField(max_length=200, unique=True, verbose_name='Заголовок')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.title


class Publication(models.Model):
    """Модель для публикации"""

    category = models.ForeignKey(to=PublicationCategory, null=True,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 related_name='publication_set')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(upload_to='publication_images', verbose_name='Постер')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

    def __str__(self):
        return self.title