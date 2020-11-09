from django.contrib import admin

# Register your models here.
from ims import models

admin.site.register(models.Categories)
admin.site.register(models.Suppliers)
admin.site.register(models.Product)
admin.site.register(models.Purchase)
admin.site.register(models.Stock)
admin.site.register(models.Sale)
admin.site.register(models.Expense)



