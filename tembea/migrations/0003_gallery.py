# Generated by Django 4.1 on 2023-06-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tembea', '0002_alter_services_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='Tembea/gallery/images')),
            ],
        ),
    ]
