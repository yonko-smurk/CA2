import uuid
from django.urls import reverse
from django.db import models



class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    def __str__(self):
        return f"{self.name} "
    
    name =  models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'category/', blank=True)


    class Meta:
        ordering =  ('name',)
        verbose_name = 'category'
        verbose_name_plural ='categories'

    def get_absolute_url(self):
        return reverse('shop:stocks_by_category', args=[self.id])
    

class Stock(models.Model):      
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False) 
    
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to = 'stock', blank=True)
    inventory = models.IntegerField() #stocks
    available =  models.BooleanField(default=True)
    created =  models.DateTimeField(auto_now_add=True, blank = True, null = True)
    updated =  models.DateTimeField(auto_now =True, blank =True, null= True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'stock'
        verbose_name_plural =  'stock'


    def get_absolute_url(self):
        return reverse('shop:stock_detail', args=[self.category.id,self.id])


    def __str__(self):
        return self.name

