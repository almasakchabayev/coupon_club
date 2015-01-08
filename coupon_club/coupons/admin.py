from django.contrib import admin
from . import models
# Register your models here.
class DealAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'old_price',
        'new_price',
        'number_of_purchases',
        'discount',
        'conditions',
        'image_url',
        'deal_url',
    )

admin.site.register(models.Tag)
admin.site.register(models.Website)
admin.site.register(models.Deal, DealAdmin)