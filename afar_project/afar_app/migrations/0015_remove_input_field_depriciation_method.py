# Generated by Django 4.2.6 on 2023-11-30 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afar_app', '0014_remove_input_field_asset_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input_field',
            name='depriciation_method',
        ),
    ]
