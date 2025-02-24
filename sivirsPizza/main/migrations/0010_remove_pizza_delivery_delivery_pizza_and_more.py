# Generated by Django 5.1.6 on 2025-02-16 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_delivery_pizza_pizza_delivery_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='delivery',
        ),
        migrations.AddField(
            model_name='delivery',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.pizza'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='expYear',
            field=models.IntegerField(choices=[(2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049)], default=2000),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='cheese',
            field=models.CharField(choices=[('Mozzarella', 'Mozzarella'), ('Vegan', 'Vegan'), ('Low Fat Mozzarella', 'Low Fat Mozzarella'), ('Cheddar', 'Cheddar'), ('Parmesan', 'Parmesan')], default='mozzarella', max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='crust',
            field=models.CharField(choices=[('Thin', 'Thin'), ('Thick', 'Thick'), ('Stuffed', 'Stuffed'), ('Neapolitan', 'Neapolitan')], default='normal', max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sauce',
            field=models.CharField(choices=[('Tomato', 'Tomato'), ('Marinara', 'Marinara'), ('Alfredo', 'Alfredo'), ('BBQ', 'BBQ')], default='tomato', max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Extra Large', 'Extra Large')], default='medium', max_length=20),
        ),
    ]
