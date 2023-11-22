from django.contrib import admin
from .models import Category, Product, Supplier, Purchase, PurchaseItem

admin.site.register(Category)
admin.site.register(Product)

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 0
    can_delete = False

class PurchaseAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    inlines = [PurchaseItemInline]

admin.site.register(Supplier)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem)