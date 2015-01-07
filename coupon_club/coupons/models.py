from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Deal(models.Model):
    title = models.TextField(default='')
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    number_of_purchases = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    conditions = models.TextField(default=0)
    # tag = models.ManyToManyField(Tag, blank=True)
    image_url = models.URLField(default='')
    deal_url = models.URLField(default='')
    website = models.URLField(default='')