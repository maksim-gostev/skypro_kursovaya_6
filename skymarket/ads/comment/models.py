from django.db import models

from skymarket.ads.ad.models import Ad
from skymarket.users.models import User




class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.TextField(verbose_name="Текст комментария")
    author = models.ForeignKey(User, verbose_name="Автор комментария", related_name='comments',
                               on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, verbose_name="Объявление", related_name='comments',
                           on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
