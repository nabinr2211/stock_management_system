from django.db import models


# Create your models here.

# model for the Categories
class Categories(models.Model):
    categories = models.CharField(max_length=100)

    def __str__(self):
        return self.categories


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.product_name


class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_numbers = models.IntegerField()
    pan_number = models.IntegerField(null=True)

    def __str__(self):
        return self.supplier_name


class Purchase(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    supplier = models.ManyToManyField(Suppliers)
    invoice_number = models.IntegerField()
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product_name)


class Stock(models.Model):
    product_name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product_name)


class Sale(models.Model):
    date = models.DateField(auto_now_add=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product_name)


class Expense(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    expenses_name = models.CharField(max_length=150)
    quantity = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-date', ]

    def __str__(self):
        return self.expenses_name
