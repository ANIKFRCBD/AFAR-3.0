# Generated by Django 4.2.9 on 2024-02-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entryfinder_sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asset_Code', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='sales_entry_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asset_code', models.CharField(null=True)),
                ('Number', models.IntegerField(null=True)),
                ('Sales_proceeds', models.FloatField(null=True)),
                ('Financial_year', models.CharField(null=True)),
                ('Year_elapsed', models.IntegerField(null=True)),
            ],
        ),
    ]
