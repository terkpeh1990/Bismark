# Generated by Django 3.0.3 on 2023-01-31 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listing', '0004_auto_20230131_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicallistings',
            name='owner_id',
        ),
        migrations.RemoveField(
            model_name='listings',
            name='owner_id',
        ),
        migrations.AddField(
            model_name='historicallistings',
            name='user_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listings',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]