from django.urls import path
from .views import SearchResultsListView, filterView
from. import views


app_name='search_app'

urlpatterns = [
    path('', SearchResultsListView.as_view(), name='searchResult'),
    path('', views.filterView, name =  'filter_search'),
]

