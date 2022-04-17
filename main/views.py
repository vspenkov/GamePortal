from django.shortcuts import render

from .models import Category, Ads, Response, User, RichTextUploadingField
from django.views.generic import ListView, DetailView
from .filters import AdsFilter


# Create your views here.
class AdssView(ListView):
    '''Вывод всех объявлений на главной странице'''
    model = Ads
    ordering = '-data_create'
    template_name = 'main.html'
    context_object_name = 'adss'
    paginate_by = 10



class AddsDetail(DetailView):
    model = Ads
    template_name = 'ads_detail.html'
    context_object_name = 'ads'
    pk_url_kwarg = 'id'


class AddsSearch(ListView):
    """Фильтр и поиск объявлений"""
    model = Ads
    template_name = 'ads_search.html'
    context_object_name = 'search'
    queryset = Ads.objects.order_by('-data_create')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Для добавления новой переменной на страницу (filter)"""
        context = super().get_context_data(**kwargs)
        context['filters'] = AdsFilter(self.request.GET, queryset=self.get_queryset())
        return context
