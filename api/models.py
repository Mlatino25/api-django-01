# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    unit_number = models.CharField(max_length=20, blank=True, null=True)
    street_number = models.CharField(max_length=20, blank=True, null=True)
    address_line1 = models.CharField(max_length=500, blank=True, null=True)
    address_line2 = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Country(models.Model):
    country_name = models.CharField(unique=True, max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class OrderLine(models.Model):
    product_item = models.ForeignKey('ProductItem', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('ShopOrder', models.DO_NOTHING, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_line'


class OrderStatus(models.Model):
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_status'


class PaymentType(models.Model):
    value = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_type'


class Product(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    product_image = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategory(models.Model):
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    category_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductConfiguration(models.Model):
    product_item = models.ForeignKey('ProductItem', models.DO_NOTHING, blank=True, null=True)
    variation_option = models.ForeignKey('VariationOption', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_configuration'


class ProductItem(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    sku = models.CharField(max_length=20, blank=True, null=True)
    qty_in_stock = models.IntegerField(blank=True, null=True)
    product_image = models.CharField(max_length=1000, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_item'


class Promotion(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    discount_rate = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotion'


class PromotionCategory(models.Model):
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    promotion = models.ForeignKey(Promotion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotion_category'


class ShippingMethod(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_method'


class ShopOrder(models.Model):
    user = models.ForeignKey('SiteUser', models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    payment_method = models.ForeignKey('UserPaymentMethod', models.DO_NOTHING, blank=True, null=True)
    shipping_address = models.ForeignKey(Address, models.DO_NOTHING, db_column='shipping_address', blank=True, null=True)
    shipping_method = models.ForeignKey(ShippingMethod, models.DO_NOTHING, db_column='shipping_method', blank=True, null=True)
    order_total = models.IntegerField(blank=True, null=True)
    order_status = models.ForeignKey(OrderStatus, models.DO_NOTHING, db_column='order_status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_order'


class ShoppingCart(models.Model):
    user = models.ForeignKey('SiteUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_cart'


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, models.DO_NOTHING, blank=True, null=True)
    product_item = models.ForeignKey(ProductItem, models.DO_NOTHING, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_cart_item'


class SiteUser(models.Model):
    username = models.CharField(max_length=350, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_user'


class UserAddress(models.Model):
    user = models.ForeignKey(SiteUser, models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_address'


class UserPaymentMethod(models.Model):
    user = models.ForeignKey(SiteUser, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.ForeignKey(PaymentType, models.DO_NOTHING, blank=True, null=True)
    provider = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_payment_method'


class UserReview(models.Model):
    user = models.ForeignKey(SiteUser, models.DO_NOTHING, blank=True, null=True)
    ordered_product = models.ForeignKey(OrderLine, models.DO_NOTHING, blank=True, null=True)
    rating_value = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_review'


class Variation(models.Model):
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variation'


class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, models.DO_NOTHING, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variation_option'
