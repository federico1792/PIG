from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.urls import reverse_lazy
from .forms import CategoryForm, ProductForm, UpdateProductForm, SupplierForm, PurchaseForm, PurchaseItemForm, FechaForm
from .models import Category, Product, Supplier, Purchase, PurchaseItem
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from portal.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
import json


##############################
##### FILTRO PARA GRUPOS #####
##############################


def grupo_administrador(user):
    return user.is_superuser or user.groups.filter(name='Admin').exists()


###############################
##### TABS ADMINISTRACION #####
###############################


######################################### INDEX #########################################
@login_required
@user_passes_test(grupo_administrador, login_url='index', redirect_field_name=None)
def index(request):
    fechas = FechaForm()
    bar_chart_data = {
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        'datasets': [
            {
                'label': 'Gastos compras',
                'backgroundColor': 'rgba(60,141,188,0.9)',
                'borderColor': 'rgba(60,141,188,0.8)',
                'pointRadius': False,
                'pointColor': '#3b8bba',
                'pointStrokeColor': 'rgba(60,141,188,1)',
                'pointHighlightFill': '#fff',
                'pointHighlightStroke': 'rgba(60,141,188,1)',
                'data': [1, 2, 3, 4, 5, 6, 7]
            },
        ]
    }

    # Convierte el diccionario a formato JSON
    bar_chart_data_json = json.dumps(bar_chart_data)
    if request.method == 'POST':
        fecha1 = request.POST['fecha_uno']
        fecha2 = request.POST['fecha_dos']
        listado = Purchase.objects.filter(date__range=(fecha1, fecha2))
        return render(request, './administracion/index.html', {'bar_chart_data': bar_chart_data_json, 'fecha': fechas, 'listado': listado})
    else:
        return render(request, './administracion/index.html', {'bar_chart_data': bar_chart_data_json, 'fecha': fechas})
######################################### INDEX #########################################


######################################### INVENTARIO ####################################
@login_required
@user_passes_test(grupo_administrador, login_url='index', redirect_field_name=None)
def inventory_view(request):
    total_products = Product.objects.all()
    latest_added = Product.objects.all().order_by('-id')[:5]
    total_categories = Category.objects.all()
    return render(request, './administracion/products/inventory.html', {'latest_added': latest_added, 'total_products': total_products,'total_categories': total_categories})
######################################### INVENTARIO ####################################


######################################### COMPRAS #######################################
@login_required
@user_passes_test(grupo_administrador, login_url='index', redirect_field_name=None)
def purchases_view(request):
    total_purchases = Purchase.objects.all()
    total_suppliers = Supplier.objects.all()
    return render(request, './administracion/purchases/purchases.html', {'total_purchases': total_purchases, 'total_suppliers': total_suppliers})
######################################### COMPRAS #######################################


######################################### USUARIOS ######################################
######################################### USUARIOS ######################################


######################################### VENTAS ########################################
######################################### VENTAS ########################################


######################
##### CATEGORIAS #####
######################


class CategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = './administracion/categories/list_categories.html'

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = './administracion/categories/add_category.html'
    success_url = reverse_lazy('add-category')
    success_message = "La categoria se creo exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = './administracion/categories/upd_category.html'
    success_url = reverse_lazy('list-categories')
    success_message = "La categoria se modifico exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Category
    template_name = './administracion/categories/del_category.html'
    success_url = reverse_lazy('list-categories')
    success_message = "La categoria se elimino exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

#####################
##### PRODUCTOS #####
#####################


@login_required
@user_passes_test(grupo_administrador, login_url='index', redirect_field_name=None)
def list_products_view(request):
    query = Product.objects.all()
    return render(request, './administracion/products/list_products.html', {'products': query})


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = './administracion/products/add_product.html'
    success_url = reverse_lazy('add-product')
    success_message = "El producto se creo exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = UpdateProductForm
    template_name = './administracion/products/upd_product.html'
    success_url = reverse_lazy('list-products')
    success_message = "El producto se modifico exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Product
    template_name = './administracion/products/del_product.html'
    success_url = reverse_lazy('list-products')
    success_message = "El producto se elimino exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class ProductDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Product
    template_name = './administracion/products/det_product.html'

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class SupplierListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Supplier
    queryset = Supplier.objects.all()
    template_name = './administracion/suppliers/list_suppliers.html'

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

#######################
##### PROVEEDORES #####
#######################


class SupplierCreateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = './administracion/suppliers/add_supplier.html'
    success_url = reverse_lazy('add-supplier')
    success_message = "El proveedor se creo exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class SupplierUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = './administracion/suppliers/upd_supplier.html'
    success_url = reverse_lazy('list-suppliers')
    success_message = "El proveedor se modifico exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class SupplierDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Supplier
    template_name = './administracion/suppliers/del_supplier.html'
    success_url = reverse_lazy('list-suppliers')
    success_message = "El proveedor se elimino exitosamente"

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

class SupplierDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Supplier
    template_name = './administracion/suppliers/det_supplier.html'

    def test_func(self):
        return grupo_administrador(self.request.user)
    
    def handle_no_permission(self):
        return redirect('index')
    

###################
##### COMPRAS #####
###################


@login_required
@user_passes_test(grupo_administrador, login_url='index', redirect_field_name=None)
def list_purchases(request):
    purchases = Purchase.objects.all()
    return render(request, './administracion/purchases/list_purchases.html', {'purchases': purchases})


@login_required
@user_passes_test(grupo_administrador, login_url='index', redirect_field_name=None)
def add_purchase(request):
    PurchaseItemFormSet = formset_factory(PurchaseItemForm)
    if request.method == "POST":
        purchase = PurchaseForm(request.POST)
        formset = PurchaseItemFormSet(request.POST)
        if formset.is_valid() and purchase.is_valid():
            purchase_instance = purchase.save()
            for form in formset:
                if form.is_valid() and form.cleaned_data.get('quantity'):
                    purchase_item = form.save(commit=False)
                    purchase_item.purchase = purchase_instance
                    purchase_item.save()
                    purchase_instance.total = purchase_instance.total + purchase_item.total
                    code = purchase_item.product.code
                    product = Product.objects.get(code=code)
                    product.stock = product.stock + purchase_item.quantity
                    product.cost_price = purchase_item.price
                    product.save()
                    purchase_instance.save()
            return redirect('list-purchases')
    else:
        purchase = PurchaseForm()
        formset = PurchaseItemFormSet()
    return render(request, "./administracion/purchases/add_purchase.html", {"formset": formset, "purchaseform": purchase})


@login_required
@user_passes_test(grupo_administrador, login_url='index', redirect_field_name=None)
def detail_purchase(request, pk):
    purchase_item = PurchaseItem.objects.all()
    my_dict = {}
    for purchase in purchase_item:
        if purchase.purchase not in my_dict.keys():
            my_dict[purchase.purchase] = [(purchase.product, purchase.quantity, purchase.price, purchase.total)]
        else:
            my_dict[purchase.purchase].append((purchase.product, purchase.quantity, purchase.price, purchase.total))
    el_dict = {}
    total = 0
    for key, value in my_dict.items():
        if pk == key.pk:
            total = key.total
            el_dict[key] = []
            for v in value:
                el_dict[key].append((v[0], v[1], v[2], v[3]))
    return render(request, './administracion/purchases/det_purchase.html', {'dict': el_dict, 'total': total})


####################
##### USUARIOS #####
####################


@login_required
@staff_member_required
def list_users(request):
    queryset = User.objects.prefetch_related('groups').all()
    all_groups = Group.objects.all()
    return render(request, './administracion/usuarios/list_users.html', {'queryset': queryset, 'all_groups': all_groups})


@login_required
@staff_member_required
def update_group(request, user_id):
    if request.method == 'POST':
        nuevo_grupo_id = request.POST.get('grupo')
        nuevo_grupo = Group.objects.get(pk=nuevo_grupo_id)
        usuario = User.objects.get(pk=user_id)
        usuario.groups.set([nuevo_grupo])
        return redirect('list-users')