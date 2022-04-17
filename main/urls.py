from django.urls import path
from .views import AdssView, AddsDetail, AddsSearch


urlpatterns =[
    path('', AdssView.as_view()),
    path('<int:id>',AddsDetail.as_view()),
    path('search/', AddsSearch.as_view(), name = 'search')

]