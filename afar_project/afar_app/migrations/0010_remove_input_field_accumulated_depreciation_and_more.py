# Generated by Django 4.1.7 on 2023-06-25 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afar_app', '0009_input_field_price_input_field_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input_field',
            name='accumulated_depreciation',
        ),
        migrations.RemoveField(
            model_name='input_field',
            name='asset_code_generated',
        ),
        migrations.RemoveField(
            model_name='input_field',
            name='costs_of_asset_sold',
        ),
        migrations.RemoveField(
            model_name='input_field',
            name='current_balance',
        ),
        migrations.RemoveField(
            model_name='input_field',
            name='current_depreciation',
        ),
    ]