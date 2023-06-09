# Generated by Django 4.1 on 2023-05-04 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'category',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('subcategory_name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
            options={
                'verbose_name_plural': 'subcategory',
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('variation', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategory')),
            ],
            options={
                'verbose_name_plural': 'variation',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_available', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='images/products')),
                ('Subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategory')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.variation')),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
    ]
