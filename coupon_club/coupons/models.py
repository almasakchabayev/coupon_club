from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Website(models.Model):
    name = models.CharField(max_length=255)
    start_url = models.CharField(max_length=255)


class Company(models.Model):
    name = models.CharField(max_length=255)


class Deal(models.Model):
    title = models.TextField()
    price = models.FloatField()
    end_date_time = models.DateTimeField()
    number_of_purchases = models.IntegerField(default=0)
    discount_percentage = models.IntegerField()
    discount_text = models.CharField(max_length=255, blank=True) #up to, from, etc.
    description = models.TextField()
    category = models.ForeignKey(Company, related_name='deals')
    tag = models.ManyToManyField(Tag, blank=True)
    deal_url = models.CharField(max_length=255)
    website = models.ForeignKey(Website, related_name='deals')


class Phone(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='phones')


class Address(models.Model):
    address_line = models.TextField()
    company = models.ForeignKey(Company, related_name='addresses')