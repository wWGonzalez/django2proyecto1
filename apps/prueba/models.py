from django.db import models

# Create your models here.

class Categoria(models.Model):
    cat= models.CharField(max_length=50)

    def __str__(self):
        return self.cat

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precioCompra = models.FloatField()
    precioVenta = models.FloatField()

    def __str__(self):
        return self.nombre
