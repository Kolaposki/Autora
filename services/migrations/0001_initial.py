# Generated by Django 3.2.8 on 2022-05-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('minamount', models.IntegerField(blank=True, default=3, null=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discount_percentage', models.IntegerField(default=0)),
                ('discount_price', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12)),
            ],
        ),
    ]
