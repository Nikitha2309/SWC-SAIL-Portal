# Generated by Django 2.2.12 on 2021-07-22 09:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210722_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bg_image_link',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
