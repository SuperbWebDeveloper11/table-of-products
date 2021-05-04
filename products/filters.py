import django_filters
from .models import Product


# we'll use this class to filter products based on model attributes
class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = {
                'title': ['icontains', ],
                'product_type': ['icontains', ],
                'height': ['gte', 'lte'],
                'width': ['gte', 'lte'],
                'price': ['gte', 'lte'],
        }

