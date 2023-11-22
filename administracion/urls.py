from django.urls import path
#pestañas nav admin
from .views import index, inventory_view, purchases_view
# restantes
from .views import list_products_view, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView,CategoryListView ,CategoryCreateView, CategoryUpdateView, CategoryDeleteView, list_purchases, add_purchase, detail_purchase, SupplierCreateView, SupplierDeleteView, SupplierDetailView, SupplierUpdateView, SupplierListView, list_users, update_group


urlpatterns = [
    #admin view
    path('', index, name='indexadmin'),
    path('inventario/', inventory_view, name='inventory'),
    path('compras/', purchases_view, name='purchases'),
    #categories
    path('listado-categorias/', CategoryListView.as_view(), name='list-categories'),
    path('agregar-categoria/', CategoryCreateView.as_view(), name='add-category'),
    path('modificar-categoria/<int:pk>', CategoryUpdateView.as_view(), name='upd-category'),
    path('eliminar-categoria/<int:pk>', CategoryDeleteView.as_view(), name='del-category'),
    #products
    path('listado-productos/', list_products_view, name='list-products'),
    path('agregar-producto/', ProductCreateView.as_view(), name='add-product'),
    path('modificar-producto/<int:pk>', ProductUpdateView.as_view(), name='upd-product'), 
    path('eliminar-producto/<int:pk>', ProductDeleteView.as_view(), name='del-product'), 
    path('detalle-producto/<int:pk>', ProductDetailView.as_view(), name='det-product'),
    #suppliers
    path('listado-proveedores/', SupplierListView.as_view(), name='list-suppliers'),
    path('agregar-proveedor/', SupplierCreateView.as_view(), name='add-supplier'),
    path('modificar-proveedor/<int:pk>', SupplierUpdateView.as_view(), name='upd-supplier'), 
    path('eliminar-proveedor/<int:pk>', SupplierDeleteView.as_view(), name='del-supplier'),
    path('detalle-proveedor/<int:pk>', SupplierDetailView.as_view(), name='det-supplier'),
    #purchases
    path('listado-compras/', list_purchases, name='list-purchases'),
    path('agregar-compra/', add_purchase, name='add-purchase'),
    path('detalle-compra/<int:pk>', detail_purchase, name='det-purchase'),
    #users
    path('usuarios/', list_users, name='list-users'),
    path('cambiar-grupo/<int:user_id>/', update_group, name='upd-group'),
]