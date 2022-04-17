from django.contrib import admin
from .models import Category, Ads, Response

# Register your models here.

admin.site.register(Category)
admin.site.register(Ads)
admin.site.register(Response)