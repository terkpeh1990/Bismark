# Generated by Django 3.0.3 on 2023-02-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_auto_20230203_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrents',
            name='ref',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='rents',
            name='ref',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
