from rest_framework import serializers

from skymarket.ads.ad.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializers.ReadOnlyField(source="author.phone")
    author_id = serializers.ReadOnlyField(source="author.id")


    class Meta:
        model = Ad
        fields = ['pk', 'title', 'price', 'description', 'image', 'author_first_name', 'author_last_name', 'phone', 'author_id']


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['image', 'title', 'price', 'description']