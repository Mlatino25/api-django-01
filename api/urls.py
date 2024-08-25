from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CategoriaProductoViewSet, ProductoViewSet, CarritoComprasViewSet, FacturasViewSet, FacturaProductosUsuariosViewSet, ImagenViewSet, InventarioViewSet, SubcategoriaProductoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaProductoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'carritos', CarritoComprasViewSet)
router.register(r'facturas', FacturasViewSet)
router.register(r'factura-productos', FacturaProductosUsuariosViewSet)
router.register(r'imagenes', ImagenViewSet)
router.register(r'inventarios', InventarioViewSet)
router.register(r'subcategorias', SubcategoriaProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
