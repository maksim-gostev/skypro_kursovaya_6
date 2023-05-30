from django.db import models

from skymarket.users.models import User



class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название товара",
                             help_text="Введите название товара (максимум 100 символов)")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена товара",
                                        help_text="Введите цену на товар")
    description = models.TextField(verbose_name="Описание товара", help_text="Опишите товар")
    author = models.ForeignKey(User ,related_name="ads", verbose_name="Автор", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    image = models.ImageField(null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ("-created_at",)
