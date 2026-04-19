from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from vouchers.models import Voucher


class Transaction(models.Model):
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2,
    verbose_name='Euro Transaction Total') 

    emailAddress = models.EmailField(max_length=250, blank=True,
verbose_name='Email Address') 
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank=True)
    billingAddress1 = models.CharField(max_length=250, blank=True)
    billingCity = models.CharField(max_length=250, blank=True)
    billingPostcode = models.CharField(max_length=10, blank=True)
    billingCountry = models.CharField(max_length=200, blank=True)
    shippingName = models.CharField(max_length=250, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=250, blank=True)
    shippingPostcode = models.CharField(max_length=10, blank=True)
    shippingCountry = models.CharField(max_length=200, blank=True)
    voucher = models.ForeignKey(Voucher, related_name='transactions', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(100)])


    class Meta:
        db_table = 'Transaction'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class TransactionItem(models.Model):
    stock = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2,
verbose_name='Euro Price')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TransactionItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.stock


