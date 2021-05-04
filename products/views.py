from django.shortcuts import render

from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin

from .models import Product
from .filters import ProductFilter
from .tables import ProductTable



# products filter
def products_filter(request):
    product_list = Product.objects.all()
    f = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'products/products_filter.html', {'filter': f})


# products table (support sorting)
class ProductsTableView(SingleTableView):
    table_class = ProductTable
    queryset = Product.objects.all()
    template_name = "products/products_table.html"


# products table (support sorting) and filter --- function based ---
def products_table_filter(request):
    product_list = Product.objects.all()
    f = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'products/products_table_filter.html', {'filter': f})


# products table (support sorting) and filter --- class based ---
class ProductsTableFilterView(SingleTableMixin, FilterView):
    table_class = ProductTable
    queryset = Product.objects.all()
    template_name = "products/products_table_filter2.html"
    filterset_class = ProductFilter


# products datatable (js datatable)
def products_datatable(request):
    product_list = Product.objects.all()
    return render(request, 'products/products_datatable.html', {'product_list': product_list})


