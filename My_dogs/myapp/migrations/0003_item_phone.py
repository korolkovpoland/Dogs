# Generated by Django 5.0 on 2023-12-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
