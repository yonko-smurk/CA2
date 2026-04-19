from django.urls import path
from . import views

app_name = 'transaction'

urlpatterns = [
    path('thanks/<int:transaction_id>/', views.thanks, name='thanks'),
    path('history/', views.transactionHistory.as_view(), name='transactions_history'),
    path('<int:transaction_id>/', views.transactionDetail.as_view(), name='transaction_detail'),
]