# Generated by Django 5.0.3 on 2024-03-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='barcode',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='الباركود'),
        ),
    ]
