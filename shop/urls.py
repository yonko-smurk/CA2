from django.urls import path
from .views import *
from django.conf import settings
from . import views



app_name = 'shop'

urlpatterns = [
    path('', views.stock_list, name = 'all_stocks'),
    path('<uuid:category_id>/', views.stock_list, name = 'stocks_by_category'),
    path('<uuid:category_id>/<uuid:stock_id>/',views.stock_detail,name= 'stock_detail'),
    path('new/',StockCreateView.as_view(), name='stock_create'),
    path('terms/',TermsAndConditionsView.as_view(), name='terms'),
    
]

# Might need this incase i mess up
# path('', stock_list, name='stock_list'),
#     path('<uuid:category_id>/<uuid:product_id>/', stock_detail, name = 'stock_detail'),
    