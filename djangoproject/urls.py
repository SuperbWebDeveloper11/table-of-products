from django.contrib import admin
from django.urls import path, include
from django_filters.views import FilterView
from products import views as product_views
from products.filters import ProductFilter


urlpatterns = [

    path('', include('products.urls')),
    path('admin/', admin.site.urls),

]


