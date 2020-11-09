from django import forms
from ims.models import Purchase, Suppliers, Product, Categories, Sale


class AddCategoriesModelsForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'


class AddProductModelsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class AddSupplierModelsForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'


class AddPurchaseModelsForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'


class AddSaleModelsForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
