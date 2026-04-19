from django.shortcuts import render, get_object_or_404
from .models import Transaction, TransactionItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

def thanks(request, transaction_id):
    if transaction_id:
        customer_transaction = get_object_or_404(Transaction, id=transaction_id)
    return render(request, 'thanks.html',{'customer_transaction': customer_transaction}) 

class transactionHistory(LoginRequiredMixin, View):
    def get (self, request):
        if request.user.is_authenticated:
            email = str(request.user.email)
            transaction_details = Transaction.objects.filter(emailAddress=email)
        return render(request, 'transaction/transactions_history.html', {'transaction_details': transaction_details})

class transactionDetail(LoginRequiredMixin, View):
    def get(self, request, transaction_id):
        if request.user.is_authenticated:
            email = str(request.user.email)
            transaction = Transaction.objects.get(id=transaction_id, emailAddress=email)
            transaction_items = TransactionItem.objects.filter(transaction=transaction)
        return render(request, 'transaction/transaction_detail.html', {'transaction': transaction, 'transaction_items': transaction_items})
        
        