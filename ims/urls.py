from django.urls import path

from ims import views

app_name = 'ims'
urlpatterns = [
    path('add-categories/', views.add_categories, name='add_categories'),
    path('categories-list/', views.categories_list, name='categories_list'),
    path('add-product/', views.add_product, name='add_product'),
    path('product-list/', views.product_list, name='product_list'),

    path('add-suppliers/', views.add_suppliers, name='add_supplier'),
    path('suppliers-list/', views.suppliers_list, name='supplier_list'),

    path('add-purchase/', views.add_purchase, name='add_purchase'),
    path('purchase-list/', views.purchase_list, name="purchase_list"),
    path('daily-purchase-list/', views.daily_purchase, name="daily_purchase_list"),
    path('monthly-purchase-list/', views.monthly_purchase, name="monthly_purchase_list"),

    path('add-sales/', views.add_sales, name='add_sales'),
    path('sales-list/', views.sale_list, name="sales_list"),
    path('daily-sales-list/', views.daily_sales, name="daily_sales_list"),
    path('monthly-sales-list/', views.monthly_sale, name="monthly_sales_list"),

]
