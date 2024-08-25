from rest_framework import serializers
from .models import Usuario, CategoriaProducto, Producto, CarritoCompras, Facturas, FacturaProductosUsuarios, Imagen, Inventario, SubcategoriaProducto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoCompras
        fields = '__all__'

class FacturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturas
        fields = '__all__'

class FacturaProductosUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaProductosUsuarios
        fields = '__all__'

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class SubcategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcategoriaProducto
        fields = '__all__'
