from django.db.models import Manager, Sum


class ProductManager(Manager):
    def in_stock(self, *args, **kwargs):
        return

    def currency_value(self, currency: str):
        return


class ProductInfoManager(Manager):
    def total_price(self):
        return self.model.all()
