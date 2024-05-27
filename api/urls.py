from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'order_lines', OrderLineViewSet)
router.register(r'order_statuses', OrderStatusViewSet)
router.register(r'payment_types', PaymentTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_categories', ProductCategoryViewSet)
router.register(r'product_configurations', ProductConfigurationViewSet)
router.register(r'product_items', ProductItemViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'promotion_categories', PromotionCategoryViewSet)
router.register(r'shipping_methods', ShippingMethodViewSet)
router.register(r'shop_orders', ShopOrderViewSet)
router.register(r'shopping_carts', ShoppingCartViewSet)
router.register(r'shopping_cart_items', ShoppingCartItemViewSet)
router.register(r'site_users', SiteUserViewSet)
router.register(r'user_addresses', UserAddressViewSet)
router.register(r'user_payment_methods', UserPaymentMethodViewSet)
router.register(r'user_reviews', UserReviewViewSet)
router.register(r'variations', VariationViewSet)
router.register(r'variation_options', VariationOptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
