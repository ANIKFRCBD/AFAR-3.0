# Generated by Django 4.2.7 on 2024-11-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_asset_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('economic_code', models.CharField(max_length=100)),
                ('expected_life_pre', models.IntegerField()),
                ('expected_life_post', models.IntegerField()),
                ('depreciation_method', models.CharField(max_length=100)),
            ],
        ),
    ]
