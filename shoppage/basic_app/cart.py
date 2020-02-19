    #******************* __CART__CLASS__ *******************#

    class cart_alias_param:
        items = {}
        total_qty = 0
        total_price = 0
        total_promt_price = 0

    class cart:
        def __init__(self,old_cart = cart_alias_param() ):
            self.items = old_cart.items
            self.total_qty = old_cart.total_qty
            self.total_price = old_cart.total_price
            self.total_promt_price = old_cart.total_promt_price

        def add(self,prod,qty):
            cur_prod_cart = {
                    'qty':0,
                    'price':0,
                    'promt_price':0,
                    'item':prod,
            }
            if prod.id in self.items:
                # if exist id in dict-> get this of thid id in dict
                cur_prod_cart =  self.items[prod.id]

            cur_prod_cart['qty'] += qty
            cur_prod_cart['price'] = cur_prod_cart['qty']*prod.price
            cur_prod_cart['promt_price'] = cur_prod_cart['qty']*prod.promotion_price
            self.items[prod.id] = cur_prod_cart
            self.total_qty += qty
            self.total_price += qty*cur_prod_cart['item'].price
            self.total_promt_price += qty*cur_prod_cart['item'].promotion_price



class cart:
    def __init__(self,old_cart):
        self.cart = old_cart
        # return self.cart
    def add(self,prod,qty):
        cur_prod_cart = {
                'qty':0,
                'price':0,
                'promt_price':0,
        }
        id = str(prod.id)
        if id in self.cart['items']:
            # if exist id in dict-> get this of thid id in dict else start from '0'
            cur_prod_cart =  self.cart['items'][id]
        cur_prod_cart['qty'] += qty
        cur_prod_cart['price'] = cur_prod_cart['qty']*prod.price
        cur_prod_cart['promt_price'] = cur_prod_cart['qty']*prod.promotion_price
        self.cart['items'][id] = cur_prod_cart # Assing value
        self.cart['total_qty'] += qty
        self.cart['total_price'] += qty*prod.price
        self.cart['total_promt_price'] += qty*prod.promotion_price
        return

if request.is_ajax():
    id = str(request.GET.get('id'))
    qty = int(request.GET.get('qty'))
    prod = Products.objects.get(id  =  id)
        # if there is NO session use "cart_alias"
    cart_alias = {
        'items':{
                    id :{
                        'qty':0,
                        'prods_price':0,
                        'prods_promt_price':0,
                    }
                        },
        'total_qty':0,
        'total_promt_price':0,
        'total_price':0,
    }
    print('_'*20,'$$_cart_alias_$$','_'*20,'\n')
    pprint(cart_alias)
    print('\n'*2)

# if str(id) in old_cart:
#     old_cart[str(id)] += qty
# else:
#     key = str(id)
#     old_cart[key] = qty
# print('new_cart \n')
# print(old_cart)
# request.session['cart'] = old_cart
# print('_'*20,'$$_end_cycle_$$','_'*20)
