from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class UserRoles(models.TextChoices):
    # TODO закончите enum-класс для пользователя
    USER = "user", _("user")
    ADMIN = "admin", _("admin")


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    first_name = models.CharField(max_length=50, verbose_name="Имя",
                                  help_text="Введите имя (максимум 50 символов)")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия ",
                                 help_text="Введите фамилию (максимум 100 символов)")
    phone = PhoneNumberField(verbose_name="Телефон для связи",
                             help_text="Введите ваш телефон для связи")
    email = models.EmailField(unique=True, verbose_name="Выша электронная почта",
                              help_text="Укажите Вашу электронную почту")
    role = models.CharField(max_length=6, choices=UserRoles.choices, default="user",
                            verbose_name="Роль пользователя", help_text="Выбирите вашу роль")
    is_active = models.BooleanField(default=True, verbose_name="Активнасть аккаунта",
                                    help_text="Укажите активен ли аккаунт")
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

