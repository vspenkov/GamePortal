from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    '''Категории'''
    name = models.CharField(max_length = 64, unique=True, verbose_name='Название категории')

    def __str__(self):
        return f'{self.name}'


class Ads(models.Model):
    '''Объявления'''
    title = models.CharField(max_length=128, verbose_name= 'Заголовок')
    content = RichTextUploadingField(verbose_name='Содержание поста')
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    data_create = models.DateTimeField(auto_now_add = True, verbose_name='Дата создания')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.title},{self.post_category},{self.user}'

    # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
    def get_absolute_url(self):
        """Функция перенаправления пользователя после добавления или изменения данных в бд
        в данном случае - обратиться к url с именем detail, передав pk = id"""

        return reverse('detail', args=[str(self.id)])


class Response(models.Model):
    '''Отклики'''
    user_response = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь отклика')
    advertisement = models.ForeignKey(Ads, on_delete=models.CASCADE, verbose_name='Содержание отклика')
    content = models.TextField(verbose_name='Текст отклика')
    date_create = models.DateTimeField(auto_now_add = True, verbose_name='Дата создания отклика')
    response_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория отклика')
    response_add = models.BooleanField (default=False, verbose_name='Отклик добавлен')
    response_rejecct = models.BooleanField (default=False, verbose_name= 'Отклик отклонен')

    def __str__(self):
        return f'{self.user_response}, {self.content}, {self.date_create}'

