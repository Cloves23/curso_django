from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from projeto_x.core.managers import ProductManager, ProductInfoManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        abstract = True


class Person(BaseModel):
    user = models.ForeignKey(User)
    name = models.CharField(_('name'), max_length=50)
    nickname = models.CharField(_('nickname'), max_length=30)
    document = models.CharField(_('document'), max_length=16)
    phone = models.CharField(_('phone'), max_length=16)
    email = models.EmailField(_('email'))

    def __str__(self):
        return f'{self.name}'


class LegalPerson(Person):
    person = models.OneToOneField('core.Person',
                                  on_delete=models.CASCADE,
                                  parent_link=True,
                                  verbose_name=_('person'))
    state_registration = models.CharField(_('state registration'), max_length=18)
    municipal_registration = models.CharField(_('municipal registration'), max_length=18)


class NaturalPerson(Person):
    GENDER = [('M', _('Male')), ('F', _('Female')), ('O', _('Other'))]

    person = models.OneToOneField('core.Person',
                                  on_delete=models.CASCADE,
                                  parent_link=True,
                                  verbose_name=_('person'))
    birthday = models.DateField(_('birthday'))
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER)
    # nationality = models.CharField(_('nationality'), max_length=40)
    # naturalness = models.CharField(_('naturalness'), max_length=30)


class BaseUserModel(BaseModel):
    created_by = models.OneToOneField(Person,
                                      on_delete=models.PROTECT,
                                      parent_link=True,
                                      related_name='created_%(class)s',
                                      verbose_name=_('created by'))
    modified_by = models.OneToOneField(Person,
                                      on_delete=models.PROTECT,
                                      parent_link=True,
                                      related_name='modified_%(class)s',
                                      verbose_name=_('modified by'))

    class Meta:
        abstract = True


class Shop(BaseUserModel):
    owner = models.OneToOneField(Person,
                                 on_delete=models.CASCADE,
                                 related_name='shops',
                                 parent_link=True,
                                 verbose_name=_('owner'))
    name = models.CharField(_('name'), max_length=60)
    default_currency = models.CharField(_('currency'), max_length=15)
    value_increase = models.DecimalField(_('value increase'), decimal_places=3, max_digits=4)


class ShoppingList(BaseUserModel):
    shop = models.OneToOneField(Shop,
                                on_delete=models.CASCADE,
                                related_name='shoppingLists',
                                parent_link=True,
                                verbose_name=_('shop'))
    currency_used = models.CharField(_('currency used'), max_length=15)
    dolar_value = models.DecimalField(_('dolar value'), decimal_places=3, max_digits=4)
    status = models.CharField(_('status'), max_length=15)  # QUAL A UTILIDADE
    products = models.ManyToManyField('Product',
                                      related_name='shoppingLists',
                                      related_query_name='shoppingList',
                                      verbose_name=_('products'),
                                      through='ProductInfo')


class Product(BaseUserModel):

    object = ProductManager()

    shop = models.OneToOneField(Shop,
                                on_delete=models.CASCADE,
                                related_name='shops',
                                related_query_name='shop',
                                verbose_name=_('shop'))
    name = models.CharField(_('name'), max_length=60)
    price = models.DecimalField(_('price'), decimal_places=3, max_digits=4)
    currency = models.CharField(_('currency'), max_length=15)
    quantity = models.PositiveSmallIntegerField


class ProductInfo(BaseModel):

    objects = ProductInfoManager()

    quantity = models.PositiveSmallIntegerField
    price = models.DecimalField(_('price'), decimal_places=3, max_digits=4)
    currency = models.CharField(_('currency'), max_length=15)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    ShoppingList = models.OneToOneField(ShoppingList, on_delete=models.CASCADE)
