# Python program to create some product samples
import json
from .models import Product



def create_products():
    with open('products/product_samples.json', 'r') as f:

        # returns JSON object as a dictionary
        data = json.load(f) 

        # Iterating through products and add them to database
        for i in data['products']: 
            Product.objects.create(
                    title = i['title'],
                    product_type = i['type'],
                    description = i['description'],
                    height = i['height'],
                    width = i['width'],
                    price = i['price'],
                    )
            print(i['title'] + ' - was created')

        print('--- products added to database --- ')


