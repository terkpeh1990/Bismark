# Generated by Django 3.0.3 on 2023-01-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_auto_20230131_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallistings',
            name='total_bedrooms',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='listings',
            name='total_bedrooms',
            field=models.PositiveIntegerField(),
        ),
    ]
