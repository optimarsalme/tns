# Generated by Django 4.1 on 2023-05-05 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Subcategory',
            new_name='subcategory',
        ),
    ]
