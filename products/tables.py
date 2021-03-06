import django_tables2 as tables
from .models import Product

class ProductTable(tables.Table):

    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap4.html"
        fields = ("title", "product_type", "height", "width", "price")
        attrs = {"class": "table table-bordered"}


