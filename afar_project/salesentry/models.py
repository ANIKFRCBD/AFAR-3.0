from django.db import models


# Create your models here.
class sales_entry_model(models.Model):
    Asset_code=models.CharField(max_length=256,null=True)
    Number=models.IntegerField(null=True)
    Sales_proceeds=models.FloatField(max_length=256,null=True)
    Financial_year=models.CharField(max_length=256,null=True)
    Year_elapsed=models.IntegerField(null=True)
class entryfinder_sales(models.Model):
    Asset_Code=models.CharField(max_length=256,null=False)


