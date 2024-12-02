from django.db import models

# Create your models here.
class model_asset_info(models.Model):
    category = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    economic_code = models.CharField(max_length=100)
    expected_life_pre = models.IntegerField()
    expected_life_post = models.IntegerField()
    depreciation_method = models.CharField(max_length=100)