from django_filters import FilterSet, ModelMultipleChoiceFilter, CharFilter
from .models import Ads,Response, User


class AdsFilter(FilterSet):
    post_category = ModelMultipleChoiceFilter(
        field_name='post_category',
        lookup_expr='exact',
        label='Категория'
    )

    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок'
    )

    class Meta:
        model = Ads
        fields = []


# class ResponseFilter(FilterSet):
#     class Meta:
#         model = Response
#         fields = ('response_category')