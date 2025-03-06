from decimal import Decimal, ROUND_HALF_UP

class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        shopping = self.session.get('shopping')
        if not shopping:
            shopping = {}
            self.session['shopping'] = shopping
        self.shopping = shopping
    
    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.shopping:
            self.shopping[product_id] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),
                'amount': 1,
                'image': product.image.url
            }
        else:
            self.shopping[product_id]['amount'] += 1
            current_price = Decimal(self.shopping[product_id]['price'])
            product_price = Decimal(product.price)
            total_price = current_price + product_price
            rounded_price = total_price.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
            self.shopping[product_id]['price'] = str(rounded_price)
        self.save_shopping()
    
    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.shopping:
            del self.shopping[product_id]
            self.save_shopping()
    
    def less_amount(self, product):
        product_id = str(product.id)
        if product_id in self.shopping:
            if self.shopping[product_id]['amount'] > 1:
                self.shopping[product_id]['amount'] -= 1
                current_price = Decimal(self.shopping[product_id]['price'])
                product_price = Decimal(str(product.price))  
                total_price = current_price - product_price
                rounded_price = total_price.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                self.shopping[product_id]['price'] = str(rounded_price)
            else:
                self.delete(product)
            self.save_shopping()
    
    def clean(self):
        self.session['shopping'] = {}
        self.session.modified = True

    def save_shopping(self):
        self.session['shopping'] = self.shopping
        self.session.modified = True
