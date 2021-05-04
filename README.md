
### filtering-products

- table-of-products is a django project built using Django, django-filter, django-tables2, datatables, django-widget-tweaks and bootstrap
- it contains endpoints to do the following operations:
    - products filter using django-filters 
    - products table using django-tables2 
    - products table and filter using django-filters and django-tables2 
    - products table and filter using javascript datatable 
- To add some initial products to the database, i created script.py, based on this [product samples](https://github.com/wedeploy-examples/supermarket-web-example/blob/master/products.json), and i just have to open the shell and run the script:
    - python manage.py shell
    - from products import script
    - script.create_products()


This is a screenshot from the project:
![Image of products](https://github.com/pedrasfloki/table-of-products/blob/main/table-of-products.png)

