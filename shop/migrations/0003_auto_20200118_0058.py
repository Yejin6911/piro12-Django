# Generated by Django 2.2.9 on 2020-01-17 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='name',
        ),
    ]
