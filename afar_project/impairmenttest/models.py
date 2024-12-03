from django.db import models

# Create your models here.
class impairmententry_model(models.Model):
    Value_in_use=models.FloatField(max_length=256,null=True)
    Fair_value_less_cost_to_sale=models.FloatField(max_length=256,null=True)
    Asset_Code=models.CharField(max_length=256,null=True)
    Financial_year=models.CharField(max_length=256,null=True)
class entryfinderm(models.Model):
    Asset_Code=models.CharField(max_length=256,null=False)