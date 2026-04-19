from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import *
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator, EmptyPage, InvalidPage
class HomePageView(TemplateView):
    template_name = 'home.html'



def stock_list(request, category_id=None):
    print("In here")
    category = None
    stocks = Stock.objects.filter(available=True)
    for s in stocks:
        print("stock", s.name)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        stocks = Stock.objects.filter(category=category,available=True)

    paginator = Paginator(stocks,6)
    try:
        page =  int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        stocks =  paginator.page(page)
    except (EmptyPage, InvalidPage):
        stocks = paginator.page(paginator.num_pages)



    return render(request, 'shop/category.html', {'category':category, 'stks':stocks})
    

def stock_detail(request, category_id, stock_id):
    stock = get_object_or_404(Stock, category_id=category_id, id=stock_id)
    return render(request, 'shop/stock.html', {'stock':stock})

# def terms_view(request, category_id=None):
#     return render(request, 'shop/terms.html')


class StockCreateView(CreateView):
    model  = Stock
    fields = ('name', 'description' , 'category', 'price', 'image', 'inventory', 'available')
    template_name = 'shop/stock_new.html'


class TermsAndConditionsView(TemplateView):
    template_name = 'shop/terms.html'