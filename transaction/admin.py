from django.contrib import admin
from .models import Transaction, TransactionItem
class TransactionItemAdmin(admin.TabularInline):
    model =TransactionItem
    fieldsets = [
    ('Stock',{'fields':['stock'],}),
    ('Quantity',{'fields':['quantity'],}),
    ('Price',{'fields':['price'],}),
    ]
    readonly_fields = ['stock','quantity','price']
    can_delete = False
    max_num = 0
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id','billingName','emailAddress','created']
    list_display_links = ('id','billingName')
    search_fields = ['id','billingName','emailAddress']
    readonly_fields = ['id','token','total','emailAddress','created','billingName','billingAddress1'
    ,'billingCity','billingPostcode','billingCountry','shippingName','shippingAddress1',
    'shippingCity','shippingPostcode','shippingCountry']
    fieldsets = [
    ('TRANSACTION INFORMATION',{'fields': ['id','token','total','created']}),
    ('BILLING INFORMATION', {'fields':
    ['billingName','billingAddress1','billingCity','billingPostcode','billingCountry','emailAddress']}),
    ('SHIPPING INFORMATION', {'fields':
    ['shippingName','shippingAddress1','shippingCity','shippingPostcode','shippingCountry']}),
    ]
    inlines = [
    TransactionItemAdmin
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
        admin.site.register(Transaction, TransactionAdmin)

admin.site.register(Transaction, TransactionAdmin)


# needs to be fixed  
# // I fixed it (I think..)
                              

