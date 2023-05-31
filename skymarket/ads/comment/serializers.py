from rest_framework import serializers

from ads.comment.models import Comment, Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    ad_id = serializers.ReadOnlyField(source="ad.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    class Meta:
        model = Comment
        fields = ['pk', 'text', 'created_at', 'author_id', 'ad_id', 'author_first_name', 'author_last_name' ]




