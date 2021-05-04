from django.contrib import admin
from django.urls import path, include
from django_filters.views import FilterView
from products import views as product_views
from products.filters import ProductFilter


urlpatterns = [

    # ---------------- products filter using django-filters ----------------  
    path('products/', product_views.products_filter, name='products_filter'),
    path('products2/', FilterView.as_view(
        filterset_class=ProductFilter, template_name='products/products_filter.html')),

    # ---------------- products table using django-tables2 ----------------  
    path('products3/', product_views.ProductsTableView.as_view()),

    # ---------------- products table and filter using django-filters and django-tables2 ----------------  
    path('products4/', product_views.products_table_filter), 
    path('products5/', product_views.ProductsTableFilterView.as_view()),

    # ---------------- using javascript datatable ----------------  
    path('products6/', product_views.products_datatable),

]


