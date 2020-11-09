import datetime

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from ims.forms import *
from ims.models import Categories


def index(request):
    return render(request, 'index.html', {})


def add_categories(request):
    if request.method == "GET":
        CategoriesForm = AddCategoriesModelsForm()
        return render(request, 'add_categories.html', {'categories_form': CategoriesForm})
    elif request.method == "POST":
        form = AddCategoriesModelsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_categories.html', {'categories_form': CategoriesForm})
        return redirect('index')
    return redirect('index')


def categories_list(request):
    categories = Categories.objects.all()
    return render(request, 'categories_list.html', {'categories': categories})


def add_product(request):
    if request.method == "GET":
        productForm = AddProductModelsForm()
        return render(request, 'add_product.html', {'product_form': productForm})
    elif request.method == "POST":
        form = AddProductModelsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_product.html', {'product_form': productForm})
        return redirect('index')
    return redirect('index')


def product_list(request):
    product = Product.objects.all()
    return render(request, 'product_list.html', {'product': product})


def add_suppliers(request):
    if request.method == "GET":
        supplierForm = AddSupplierModelsForm()
        return render(request, 'add_supplier.html', {'supplier_form': supplierForm})
    elif request.method == "POST":
        form = AddSupplierModelsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_supplier.html', {'supplier_form': supplierForm})
        return redirect('index')
    return redirect('index')


def suppliers_list(request):
    supplier = Suppliers.objects.all()
    return render(request, 'suppliers_list.html', {'supplier': supplier})


def add_purchase(request):
    if request.method == "GET":
        purchaseForm = AddPurchaseModelsForm()
        return render(request, 'add_purchase.html', {'purchase_form': purchaseForm})
    elif request.method == "POST":
        form = AddPurchaseModelsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_purchase.html', {'purchase_form': purchaseForm})
        return redirect('index')
    return redirect('index')


# view for purchase items
def purchase_list(request):
    purchase = Purchase.objects.all()
    return render(request, 'purchase_list.html', {'purchase': purchase})


# view for monthly purchase items
def daily_purchase(request):
    today = datetime.date.today()
    dailyPurchase = Purchase.objects.filter(date__month=today.month, date__day=today.day)
    return render(request, 'daily_purchase.html', {'dailyPurchase': dailyPurchase})


# VIEWS FOR MONTHLY PURCHASE
def monthly_purchase(request):
    today = datetime.date.today()
    monthlyPurchase = Purchase.objects.filter(date__year=today.year, date__month=today.month)
    return render(request, 'monthly_purchase.html', {'monthlyPurchase': monthlyPurchase})


def add_sales(request):
    if request.method == "GET":
        salesForm = AddSaleModelsForm()
        return render(request, 'add_sale.html', {'sales_form': salesForm})
    elif request.method == "POST":
        form = AddSaleModelsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_sale.html', {'sales_form': salesForm})
        return redirect('index')
    return redirect('index')


# view for purchase items
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale_list.html', {'sales': sales})


# view for monthly purchase items
def daily_sales(request):
    today = datetime.date.today()
    dailysale = Sale.objects.filter(date__month=today.month, date__day=today.day)
    return render(request, 'daily_sale.html', {'dailysales': dailysale})


# VIEWS FOR MONTHLY PURCHASE
def monthly_sale(request):
    today = datetime.date.today()
    monthlysales = Sale.objects.filter(date__year=today.year, date__month=today.month)
    return render(request, 'monthly_sales.html', {'monthlysales': monthlysales})
