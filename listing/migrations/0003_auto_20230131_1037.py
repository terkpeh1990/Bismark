# Generated by Django 3.0.3 on 2023-01-31 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20230131_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallistings',
            name='total_bathrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='historicallistings',
            name='total_bedrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='historicallistings',
            name='total_occupancy',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listings',
            name='total_bathrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listings',
            name='total_bedrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listings',
            name='total_occupancy',
            field=models.IntegerField(),
        ),
    ]