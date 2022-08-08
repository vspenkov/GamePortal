from django.contrib import admin
from django import forms
from .models import Category, Ads, Response

# Register your models here.

from ckeditor_uploader.widgets import CKEditorUploadingWidget



class AdsAdminForm(forms.ModelForm):
    content = forms.CharField(label="Содержание поста", widget=CKEditorUploadingWidget())

    class Meta:
        model = Ads
        fields = '__all__'

class AdsAdmin(admin.ModelAdmin):
    list_display = ("title", "post_category", "user")
    form = AdsAdminForm

admin.site.register(Category)
admin.site.register(Ads, AdsAdmin)
admin.site.register(Response)
