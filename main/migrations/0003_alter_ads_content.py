# Generated by Django 4.0.4 on 2022-05-17 19:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_ads_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание поста'),
        ),
    ]
