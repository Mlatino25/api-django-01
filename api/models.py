from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=350)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=500)

    class Meta:
        db_table = 'usuario'

class CategoriaProducto(models.Model):
    id = models.AutoField(primary_key=True)
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='subcategorias')
    category_name = models.CharField(max_length=200, blank=True, null=True)
    description_category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'categoria_producto'

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(CategoriaProducto, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'producto'

class CarritoCompras(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)
    email_cliente = models.CharField(max_length=255, blank=True, null=True)
    fecha_cotizacion = models.DateField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medio_pago = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'carrito_compras'

class Facturas(models.Model):
    id = models.AutoField(primary_key=True)
    numero_factura = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    nombre_cliente = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_facturacion = models.DateField(blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado_factura = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuario_id')

    class Meta:
        db_table = 'facturas'

class FacturaProductosUsuarios(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Facturas, models.DO_NOTHING)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'factura_productos_usuarios'

class Imagen(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    ruta = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'imagen'

class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    cantidad_disponible = models.IntegerField(blank=True, null=True)
    cantidad_ventas = models.IntegerField(blank=True, null=True)
    carrito_compras = models.ForeignKey(CarritoCompras, models.DO_NOTHING)

    class Meta:
        db_table = 'inventario'

class SubcategoriaProducto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(CategoriaProducto, models.DO_NOTHING)
    nombre_categoria = models.CharField(max_length=255, blank=True, null=True)
    detalle_categoria = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'subcategoria_producto'
