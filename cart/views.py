from django.shortcuts import redirect, render, get_object_or_404
from shop.models import Stock
from .models import Cart, CartItem
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from transaction.models import Transaction, TransactionItem
import stripe
from vouchers.models import Voucher
from vouchers.forms import VoucherApplyForm
from decimal import Decimal


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(stock=stock, cart=cart)
        if (cart_item.quantity < cart_item.stock.inventory):     
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(stock=stock, quantity=1,cart=cart)
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items = None):
    discount = 0
    voucher_id = 0
    new_total = 0
    voucher = None

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.stock.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total*100)
    description = 'Online Shop - New Transaction'
    date_key = settings.STRIPE_PUBLISHABLE_KEY

    voucher_apply_form = VoucherApplyForm()
    try:
        voucher_id = request.session.get('voucher_id')
        voucher = Voucher.objects.get(id=voucher_id)
        if Voucher != None:
            discount = (total*(voucher.discount/Decimal('100')))
            new_total = (total - discount)
            stripe_total = int(new_total * 100)
    except:
        ObjectDoesNotExist
        pass

    if request.method=='POST':
        print(request.POST)
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingcity = request.POST['stripeBillingAddressCity']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingcity = request.POST['stripeShippingAddressCity']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            customer = stripe.Customer.create(email=email, source=token)
            stripe.Charge.create(amount=stripe_total, currency="eur", description=description, customer=customer.id)

            try:
                transaction_details = Transaction.objects.create(
                    token = token,
                    total = total,
                    emailAddress = email,
                    billingName = billingName,
                    billingAddress1 = billingAddress1,
                    billingCity = billingcity,
                    billingCountry = billingCountry,
                    shippingName = shippingName,
                    shippingAddress1 = shippingAddress1,
                    shippingCity = shippingcity,
                    shippingCountry = shippingCountry
                    )
                transaction_details.save()
                if voucher != None:
                    transaction_details.total = new_total
                    transaction_details.voucher = voucher
                    transaction_details.discount = discount
                    transaction_details.save()
                for transaction_item in cart_items:
                    oi = TransactionItem.objects.create(
                        stock = transaction_item.stock.name,
                        quantity = transaction_item.quantity,
                        price = transaction_item.stock.price,
                        transaction = transaction_details)
                    if voucher != None:
                        discount = (oi.price*(voucher.discount/Decimal('100')))
                        oi.price = (oi.price - discount)
                    else:
                        oi.price = oi.price*oi.quantity
                    oi.save

                    stocks = Stock.objects.get(id=transaction_item.stock.id)
                    stocks.inventory = int(transaction_item.stock.inventory - 
                    transaction_item.quantity)
                    stocks.save()
                    transaction_item.delete()

                    print('The transaction has been created')
                    return redirect ('transaction:thanks', transaction_details.id)
            except ObjectDoesNotExist:
                pass
            
        except stripe.error.CardError as e:
            return e
    return render(request, 'cart.html', {'cart_items':cart_items, 'total':total, 'counter':counter,
                                        'data_key':date_key, 'stripe_total':stripe_total,
                                        'description':description, 'voucher_apply_form': voucher_apply_form,
                                        'new_total': new_total, 'voucher': voucher, 'discount': discount})
    
def cart_remove(request, stock_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    stock = get_object_or_404(Stock, id=stock_id)
    cart_item = CartItem.objects.get(stock=stock, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
    
def full_remove(request, stock_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    stock = get_object_or_404(Stock, id=stock_id)
    cart_item = CartItem.objects.get(stock=stock, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')

