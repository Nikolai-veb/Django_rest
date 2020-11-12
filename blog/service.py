from django_filters import rest_framework as filtres

from blog.models import Article


class CharFilterFilter(filtres.BaseInFilter, filtres.CharFilter,):
    pass


class DateFilterFilter(filtres.BaseInFilter, filtres.DateFilter):
    pass


class ArticleFilter(filtres.FilterSet):
    tags = CharFilterFilter(field_name='tags__name', lookup_expr='in')
    date = DateFilterFilter(field_name='date__create', lookup_expr='in')

    class Meta:
        model = Article
        fields = ['tags', 'date']