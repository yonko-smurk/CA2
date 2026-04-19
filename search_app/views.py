from shop.models import Stock
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render

class SearchResultsListView(ListView):
    model = Stock
    context_object_name = 'stock_list'
    template_name =  'search.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return Stock.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    

    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        context ['query'] =  self.request.GET.get('q')
        return context
    
def filterView(request):
        qs = Stock.objects.all()
        name_contains_query =  request.GET.get('name_contains')

        if name_contains_query != '' and name_contains_query is not None:
             qs = qs.filter(name__icontains=name_contains_query)

        context ={
             'queryset':qs,

        }
        return render(request,"search.html",{}, context)