# Generated by Django 2.2.9 on 2020-01-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200118_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photp',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
