from django.db import models

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    nombre_cat = models.CharField(max_length=80, unique=True)
    descripcion_cat = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'categoria'
        
    def __str__(self):
        return self.nombre_cat

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, unique=True)
    nombre_prod = models.CharField(max_length=120)
    descripcion_prod = models.TextField(blank=True, null=True)
    precio_prod = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    id_cat = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='productos')
    id_brand = models.ForeignKey('Marca', on_delete=models.CASCADE, related_name='productos')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'producto'
        
    def __str__(self):
        return self.nombre_prod
    
class Marca(models.Model):
    id_brand = models.AutoField(primary_key=True)
    nombre_brand = models.CharField(max_length=80, unique=True)
    sitio_web_brand = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'marca'
        
    def __str__(self):
        return self.nombre_brand
    
class Almacen(models.Model):
    id_alm = models.AutoField(primary_key=True)
    nombre_alm = models.CharField(max_length=80)
    direccion_alm = models.CharField(max_length=250, blank=True, null=True)
    ciudad_alm = models.CharField(max_length=100, blank=True, null=True)
    estado_alm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'almacen'
        
    def __str__(self):
        return self.nombre_alm


class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='inventario')
    id_alm = models.ForeignKey('Almacen', on_delete=models.CASCADE, related_name='inventario')
    cantidad = models.IntegerField()
    stock_minimo = models.IntegerField()
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'inventario'
       
    def __str__(self):
        return f'{self.id_prod.nombre_prod} - {self.id_alm.nombre_alm} - Cantidad: {self.cantidad}'