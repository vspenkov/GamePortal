from django_filters import FilterSet, ModelMultipleChoiceFilter, CharFilter
from .models import Ads, Response, User


class AdsFilter(FilterSet):
    class Meta:
        model = Ads
        fields = ['post_category', 'title']

#
# class ResponseFilter(FilterSet):
#     class Meta:
#         model = Response
#         fields = ('ads_id')