from collections.abc import Iterable
class Product:
    def __init__(self, name, price):
        self._name = name 
        self._price = price 

    @property
    def price(self):
        return self._price

class ProductBundle:
    def __init__(self,name,prec_discount,*products: Iterable[Product | "ProductBundle"]):
        self._name = name
        self._perc_discount = prec_discount
        self._products = products
    
    @property
    def price(self):
        total = sum(p.price for p in self._products)
        return total * (1 - self._perc_discount)
    