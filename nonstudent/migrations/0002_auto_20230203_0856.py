# Generated by Django 3.0.3 on 2023-02-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonstudent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalnonstudents',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nonstudents',
            name='id',
        ),
        migrations.AlterField(
            model_name='historicalnonstudents',
            name='work_contract',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='nonstudents',
            name='work_contract',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
