# Generated by Django 3.0.3 on 2023-02-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_auto_20230201_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrents',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='historicalrents',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rents',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rents',
            name='start_date',
            field=models.DateField(),
        ),
    ]
