# Generated by Django 5.1 on 2024-12-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afar_app', '0018_remove_input_field_sold_quantity_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='model_asset_info',
        ),
    ]