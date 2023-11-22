from django.forms import ModelForm
from django import forms
from .models import Category, Product, Supplier, Purchase, PurchaseItem


class FechaForm(forms.Form):
    fecha_uno = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),)
    fecha_dos = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['nombre',]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre',})
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'code': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Codigo',}),
            'category': forms.Select(attrs={'class': 'form-control category','placeholder': 'Categoria',}),
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre',}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Descripcion',}),
            "cost_price": forms.NumberInput(attrs={"class": "form-control","placeholder": '$ Costo',}),
            "sale_price": forms.NumberInput(attrs={"class": "form-control","placeholder": '$ Venta',}),
            "stock": forms.NumberInput(attrs={"class": "form-control","placeholder": 'Stock',}),
            "bar_code": forms.NumberInput(attrs={"class": "form-control","placeholder": 'Codigo de barras',}),
        }


class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('code',)

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control category','placeholder': 'Categoria',}),
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre',}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Descripcion',}),
            "cost_price": forms.NumberInput(attrs={"class": "form-control","placeholder": '$ Costo',}),
            "sale_price": forms.NumberInput(attrs={"class": "form-control","placeholder": '$ Venta',}),
            "stock": forms.NumberInput(attrs={"class": "form-control","placeholder": 'Stock',}),
            "bar_code": forms.NumberInput(attrs={"class": "form-control","placeholder": 'Codigo de barras',}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control category','placeholder': 'Nombre',}),
            'cell_phone': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Celular',}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email',}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['supplier']
        labels = {
            'supplier': 'Proveedor',
        }

class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity', 'price', 'total']
        
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Cantidad',}),
            'price': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Precio',}),
            'total': forms.TextInput(attrs={'class': 'form-control','readonly': True,}),
        }
