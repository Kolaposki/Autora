# Generated by Django 3.2.8 on 2022-05-03 13:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20220503_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
