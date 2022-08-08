from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from .models import Category, Ads, Response, User, RichTextUploadingField
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .filters import AdsFilter

from .forms import AdsForm


# Create your views here.
class AdssView(ListView):
    '''Вывод всех объявлений на главной странице'''
    model = Ads
    ordering = '-data_create'
    template_name = 'main.html'
    context_object_name = 'adss'
    paginate_by = 5



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
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        self.filterset = AdsFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self,*args, **kwargs):
        """Для добавления новой переменной на страницу (filter)"""
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AddsCreate(LoginRequiredMixin, CreateView):
    """Создание объявления"""
    template_name = 'ads_create.html'
    context_object_name = 'create'
    form_class = AdsForm



class AddsDelete(LoginRequiredMixin, DeleteView):
    """удаление объявления"""
    template_name = 'ads_delete.html'
    queryset = Ads.objects.all()
    # queryset - переопределение вывода информации на страницу

    success_url = reverse_lazy('main')



class AddsEdit(LoginRequiredMixin, UpdateView):
    """Редактирование объявления"""
    template_name = 'ads_edit.html'
    context_object_name = 'edit'
    form_class = AdsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('id')
        return Ads.objects.get(id=id)




