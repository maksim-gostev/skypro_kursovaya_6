import django_filters
from django_filters.rest_framework import FilterSet

from skymarket.ads.comment.models import Ad


class AdFilters(FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Ad
        fields = ["title"]