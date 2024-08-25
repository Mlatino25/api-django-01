from rest_framework import viewsets
from .models import Usuario, CategoriaProducto, Producto, CarritoCompras, Facturas, FacturaProductosUsuarios, Imagen, Inventario, SubcategoriaProducto
from .serializers import UsuarioSerializer, CategoriaProductoSerializer, ProductoSerializer, CarritoComprasSerializer, FacturasSerializer, FacturaProductosUsuariosSerializer, ImagenSerializer, InventarioSerializer, SubcategoriaProductoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoComprasViewSet(viewsets.ModelViewSet):
    queryset = CarritoCompras.objects.all()
    serializer_class = CarritoComprasSerializer

class FacturasViewSet(viewsets.ModelViewSet):
    queryset = Facturas.objects.all()
    serializer_class = FacturasSerializer

class FacturaProductosUsuariosViewSet(viewsets.ModelViewSet):
    queryset = FacturaProductosUsuarios.objects.all()
    serializer_class = FacturaProductosUsuariosSerializer

class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class SubcategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = SubcategoriaProducto.objects.all()
    serializer_class = SubcategoriaProductoSerializer
