# Generated by Django 5.0.2 on 2024-02-18 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_remove_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_api.customer'),
        ),
    ]
