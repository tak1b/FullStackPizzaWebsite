# Generated by Django 5.1.6 on 2025-02-15 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_pizza_cheese_alter_pizza_crust_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.pizza'),
        ),
    ]
