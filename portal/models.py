from django.contrib.auth.models import User
from django.db import models

class CuponDescuento(models.Model):
    nombre = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cupones_descuento = models.ManyToManyField(CuponDescuento, related_name='cupones', blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'