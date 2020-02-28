from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from basic_app.forms import Customers_form
from basic_app.models import ( Products,Categories,PageUrl,
                            Bills,BillDetail,Customers)
from pprint import pprint
from inspect import getmembers
from django.contrib.auth.forms import (AuthenticationForm,
                                    UserCreationForm)

from django.contrib.auth import views as auth_views
# import json
    # generate token
from django.utils.crypto import get_random_string
import uuid
    # use mail
from django.core.mail import EmailMessage
from django.core import mail
    # mail template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
    # date_time
from django.utils import timezone

# Create your views here.
def get_hearder_footer_data():
    data = {}
    all_type_name  = Categories.objects.all()
    data['prod_type'] = all_type_name
    return data



def detail(request,prod):
    context = {}
    prod_id_url = PageUrl.objects.get(url = prod) # WILL get product id_url
    prod = Products.objects.get(id_url = prod_id_url.id )   # WILL get product
    context = {
                'detail_prod': prod,
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/detail.html',context)


def index(request):
    context = {}
    featured_obj  = Products.objects.filter(status = 1)
    new_obj = Products.objects.filter(new = 1)
    context = {
                'cart': get_cart_session(request),
                'new_prods': new_obj,
                'featured_prods':featured_obj,
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/index.html',context)


def base(request):
    context = {}
    context = {
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/base.html',context)

def about(request):
    context = {}
    context = {
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/about.html',context)


def contact(request):
    context = {}
    context = {
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/contact.html',context)


def categories(request,article):
    context = {}
    url_name = PageUrl.objects.get(url = article) # find url_name
    type = Categories.objects.get(id_url = url_name.id)
    prod_in_type = Products.objects.filter(id_type = type.id)
    # for i in prod_in_type:
    #     print(i.id)
    context = {
                'prod_in_type' : prod_in_type,
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/typed_products.html',context)


def login(request):
    context = {}
    Form = AuthenticationForm
    context = {
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                'form':Form
                }
    return render(request,'basic_app/login.html',context,)


def faqs(request):
    context = {}
    context = {
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/faq.html',context)


def preview(request):
    context = {}
    context = {
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/preview.html',context)


def cart(request):
    if request.is_ajax():
        action = request.GET.get('action')
        if action == 'add':
            return JsonResponse(add_cart(request))
        elif action == 'delele_a_prod':
            return JsonResponse(delete_a_product(request))
        elif action == 'delele_all_prod':
            return JsonResponse(delete_all_product(request))
        elif action == 'update':
            return JsonResponse(update_cart(request))
    else :
        context = {}
        context = {
            'cat_names' : get_hearder_footer_data()['prod_type'],
            'cart': get_cart_session(request),
        }
        return render(request,'basic_app/shopping_cart.html',context)


    # sample_code_for_ Session
    # https://www.youtube.com/watch?v=EW_vjGzXPCc






def get_cart_session(request):
        cart = {}
        try:
            cart = request.session['cart_']
        except:
            pass


        try:
            # print('_'*20,'***___cart_session_to_render___***','_'*20,'\n')
            # pprint(cart)
            # print('\n'*2)

            #   add product_object_detail to cart_session
            for id in cart['items']:
                cart['items'][id]['item'] = Products.objects.get(id = int(id))
        except:
            pass
        return cart


def add_cart(request):
    # pass
        id = str(request.GET.get('id'))
        qty = int(request.GET.get('qty'))
        print('qty = ',qty)
        prod = Products.objects.get(id  =  id)
            # if there is NO session use "cart_alias"
        cart_alias = {
            'items':{
                id :{
                    'qty':0,
                    'price':0,
                    'promt_price':0,
                }
            },
            'total_qty':0,
            'total_promt_price':0,
            'total_price':0,
        }

        # print('_'*20,'$$_cart_alias_$$','_'*20,'\n')
        # pprint(cart_alias)
        # print('\n'*2)
        old_cart_dict = cart_alias
        try:
            old_cart_dict =request.session['cart_']
        except:
            pass
        if not bool(old_cart_dict):
            old_cart_dict = cart_alias

        # print('_'*20,'***___session_holding_cart___***','_'*20,'\n')
        # pprint(old_cart_dict)
        # print('\n'*2)
        cart_obj = cart_class(old_cart_dict)
        cart_obj.add(prod,qty)
        # print('_'*20,'***___after_add___***','_'*20,'\n')
        # pprint(cart_obj.cart)
        # print('\n'*2)
        request.session['cart_'] = cart_obj.cart

        data = {
            'success_': True,
            'message_': 'ajax is cool!',
            'prod_name': prod.name,
            'id':id,
            'qty':qty,
            'item_total_price': cart_obj.cart['items'][id]['price'],
            'item_total_promt_price': cart_obj.cart['items'][id]['promt_price'],
            'item_qty': cart_obj.cart['items'][id]['qty'],
            'total_price': cart_obj.cart['total_price'],
            'total_promt_price': cart_obj.cart['total_promt_price'],
            'total_qty':cart_obj.cart['total_qty'],
        }
        return data


class cart_class:
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
    def remove_a_prod(self,prod):
        id = str(prod.id)
        self.cart['total_qty'] -= self.cart['items'][id]['qty']
        self.cart['total_price'] -= self.cart['items'][id]['price']
        self.cart['total_promt_price'] -= self.cart['items'][id]['promt_price']
        self.cart['items'].pop(id)


    def update(self,prod,qty):
                cur_prod_cart = {
                        'qty':0,
                        'price':0,
                        'promt_price':0,
                }
                id = str(prod.id)
                if id in self.cart['items']:
                    # if exist id in dict-> get this of thid id in dict else start from '0'
                    cur_prod_cart =  self.cart['items'][id]
                old_qty = cur_prod_cart['qty']
                cur_prod_cart['qty'] = qty
                cur_prod_cart['price'] = cur_prod_cart['qty']*prod.price
                cur_prod_cart['promt_price'] = cur_prod_cart['qty']*prod.promotion_price
                self.cart['items'][id] = cur_prod_cart # Assing value
                actual_qty = qty - old_qty
                self.cart['total_qty'] += actual_qty
                self.cart['total_price'] += actual_qty*prod.price
                self.cart['total_promt_price'] += actual_qty*prod.promotion_price


def delete_a_product(request):
    id = request.GET.get('id')
    prod = Products.objects.get(id = int(id))
    cart_session = request.session['cart_']
    cart_obj = cart_class(cart_session)
    cart_obj.remove_a_prod(prod)
    # pprint(cart_session)
    request.session['cart_'] = cart_obj.cart    # cart is a attr in cart_class
    print('delete_id: ',id)
    data = {
        'success': True,
        'message': 'delete product'+prod.name,
        'id':id,
        'total_price' : cart_obj.cart['total_price'],
        'total_promt_price' : cart_obj.cart['total_price'],
        'total_qty':cart_obj.cart['total_qty'],


    }
    pprint(cart_obj.cart)
    data['cart_status'] = 'exist_cart'
    if not bool(cart_obj.cart['items']):
        data['cart_status'] = 'empty'
        request.session['cart_'] = {}
    print(data['cart_status'])
    return data


def delete_all_product(request):
    request.session['cart_'] = {}
    data = {
        'success': True,
        'message': 'delete all product',
    }
    return data


def update_cart(request):
    # pass
        id = str(request.GET.get('id'))
        qty = int(request.GET.get('qty'))
        prod = Products.objects.get(id  =  id)
        old_cart_dict =request.session['cart_']
        cart_obj = cart_class(old_cart_dict)
        cart_obj.update(prod,qty)
        request.session['cart_'] = cart_obj.cart
        data = {
            'success_': True,
            'message_': 'ajax is cool!',
            'prod_name': prod.name,
            'id':id,
            'qty':qty,
            'item_total_price': cart_obj.cart['items'][id]['price'],
            'item_total_promt_price': cart_obj.cart['items'][id]['promt_price'],
            'item_qty': cart_obj.cart['items'][id]['qty'],
            'total_price': cart_obj.cart['total_price'],
            'total_promt_price': cart_obj.cart['total_promt_price'],
            'total_qty':cart_obj.cart['total_qty'],

        }
        return data


def sign_up(request):
    context = {
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                'form':UserCreationForm()
                }
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('form is is_valid')
            context['registered'] = 'success'
            return render(request,'registration/sign_up.html',context)
        else:
            print('form is not valid')
            context['error'] = 'invalid form data'
            return render(request,'registration/sign_up.html',context)
    else:
        print('fail to ')
    return render(request,'registration/sign_up.html',context)

def checkout_mail_sent(request):
    context = {}
    context = {
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/checkout_sent_mail.html',context)

def checkout_confirm(request,token):
    # token = str(token[0])
    context = {}
    token_flag = 0
    list_token = Bills.objects.values('token')
    # pprint(list_token)
    token_dict = {'token':token}


    if token_dict in list_token:
        token_flag = 1
        # print('token : ',token_dict['token'])
    else:
        context = {

                    'confirm' : 'wrong token, failed to verify your order!',
                    'thank_you': 'please make order again!',
                    'cart': get_cart_session(request),
                    'cat_names':get_hearder_footer_data()['prod_type'],
                    }
        return render(request,'basic_app/checkout_confirm.html',context)

    if token_flag: # == token_session:
        Bill = Bills.objects.get(token = token)
        if Bill.status:
            print('status:',Bill.status)
            context = {
                        'confirm' : 'You have already verified this order!',
                        'thank_you': 'thank you',
                        'cart': get_cart_session(request),
                        'cat_names':get_hearder_footer_data()['prod_type'],
                        }
            return render(request,'basic_app/checkout_confirm.html',context)
        else:
            Bill.status = 1
            Bill.save()
            delete_all_product(request)

            context = {
                        'confirm': ' your order is confirmed',
                        'thank_you': 'Thank you for shopping',
                        'cart': get_cart_session(request),
                        'cat_names':get_hearder_footer_data()['prod_type'],
                        }
            return render(request,'basic_app/checkout_confirm.html',context)
    else:
        print('token is not in list_token of database!')
        context = {

                    'confirm' : 'failed to verify your order!',
                    'thank_you': 'please make order again!',
                    'cart': get_cart_session(request),
                    'cat_names':get_hearder_footer_data()['prod_type'],
                    }
        return render(request,'basic_app/checkout_confirm.html',context)

def checkout(request):
    success = False
    form = Customers_form()
    context = {}
    bills = {}
    customers_model = {}
    bill_detail = {}
    if request.method == 'POST':
        form = Customers_form(request.POST)
        if form.is_valid():

            ### get data
            data = form.cleaned_data
            name = data['name']
            email = data['email']
            address = data['address']
            phone = data['phone']
            gender =  data['gender']
            cart = get_cart_session(request)
            # pprint(cart)

            ### insert to Customers Model
            Customer = Customers.objects.create(
                            name  = name,
                            gender = gender,
                            email = email,
                            address = address,
                            phone = phone,
                        )
            id_customer = Customers.objects.latest()
            # print('id_customer =',id_customer.id)

            # pprint(cart)
            token = get_random_string(32)+'_time_'+str(timezone.now()) # +'_token_'+str(uuid.uuid4())
            token = token.replace(" ","_")
            token = token.replace(":","-")
            token = token.replace(".","_")
            token = token.replace("+","-")

            # request.session['token'] =   1   # {'token':str(token)}
                # insert to Customers Model
            Bill = Bills.objects.create(
                        id_customer = id_customer,
                        total = cart['total_qty'],
                        promt_price = cart['total_promt_price'],
                        token =token,
                        status = 0,
                    )
            id_bill = Bills.objects.latest()
            # print('id_bill= ',id_bill.id)

                # insert to Customers Model
            cart_items = cart['items']
            for id in cart_items:
                Bill_detail = BillDetail.objects.create(
                        id_bill = id_bill,
                        id_product = cart_items[id]['item'],    # instance
                        quantity = cart_items[id]['qty'],
                        price = cart_items[id]['item'].price,
                        discount_price = cart_items[id]['item'].promotion_price,
                        )
                id_bill_detail = BillDetail.objects.latest().id
                # print(id_bill_detail)

            subject,from_mail = " Shopping order comfirmation ",'bluenight0104@gmail.com',
            html_message = render_to_string('mail_template.html',{'token':token})
            plain_message = strip_tags(html_message)
            try:
                pass
            except Exception as e:
                raise
            mail.send_mail(subject,plain_message,from_mail,[email],html_message=html_message)

            success = True
            context = {
                        'success' : success,
                        'email':email,
                        'cart': get_cart_session(request),
                        'cat_names':get_hearder_footer_data()['prod_type'],
                        }
            render(request, 'basic_app/checkout_sent_mail.html',context)

    else:
        pass
    context = {
                'success' : success,
                'form':form,
                'cart': get_cart_session(request),
                'cat_names':get_hearder_footer_data()['prod_type'],
                }
    return render(request,'basic_app/check_out.html',context)
