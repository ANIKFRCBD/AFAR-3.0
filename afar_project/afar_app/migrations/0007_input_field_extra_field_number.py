# Generated by Django 4.1.7 on 2023-04-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afar_app', '0006_alter_input_field_financial_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_field',
            name='extra_field_number',
            field=models.IntegerField(default=0),
        ),
    ]
