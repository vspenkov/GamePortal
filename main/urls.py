from django.urls import path, include
from django.conf import settings
from .views import AdssView, AddsDetail, AddsSearch, AddsEdit, AddsDelete, AddsCreate
from django.conf.urls.static import static
# ResponseList, ResponseRemove, ResponseAccept

urlpatterns =[
    path('', AdssView.as_view(), name = 'main'),
    path('<int:id>',AddsDetail.as_view(), name='detail'),
    path('search/', AddsSearch.as_view(), name = 'search'),


    path('create/', AddsCreate.as_view(), name = 'create'),
    path('edit/<int:id>', AddsEdit.as_view(), name = 'edit'),
    path('delete/<int:pk>', AddsDelete.as_view(), name = 'delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)