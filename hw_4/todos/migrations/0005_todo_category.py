# Generated by Django 5.1.6 on 2025-02-27 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todos.category'),
        ),
    ]
