# Generated by Django 4.2.11 on 2024-04-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AddField(
            model_name='quantityofclothes',
            name='ONESIZE',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quantityofclothes',
            name='XXL',
            field=models.PositiveIntegerField(default=0),
        ),
    ]