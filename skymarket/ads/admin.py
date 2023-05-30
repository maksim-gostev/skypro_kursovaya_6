from django.contrib import admin

from skymarket.ads.comment.models import Ad, Comment

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'descriptions','author', 'created_at', 'image')


admin.register(Ad, AdAdmin)
admin.register(Comment)
