from django.db import models

#PRODUCTS
class Category(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='categoria')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    code = models.PositiveIntegerField(unique=True, verbose_name='codigo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='categoria')
    name = models.CharField(max_length=35, verbose_name='nombre')
    description = models.TextField(max_length=800, verbose_name='descripcion')
    cost_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='precio de coste')
    sale_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='precio de venta') #decimalfield para dinero siempre, float presenta errores
    stock = models.IntegerField(verbose_name='stock')
    bar_code = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='codigo de barras')
    image = models.ImageField(upload_to='product_img', null=True, verbose_name='imagen')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


#PURCHASES
class Supplier(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    cell_phone = models.IntegerField(verbose_name='Celular')
    email = models.EmailField(blank=True, verbose_name='Email')

    def __str__(self):
        return self.name

class Purchase(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.pk)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)