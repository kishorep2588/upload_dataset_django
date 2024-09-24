import json

json_input_file = 'electronics_product.json'
product_json_output_file = 'product_fixture.json'
category_json_output_file = 'category_fixture.json'

product_data = []

with open(json_input_file, 'r') as json_file:
    data = json.load(json_file)

'''
  {
    "model": "myapp.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  }
'''
import random

def get_sale_option():
    options = [1,2]
    choice = random.choice(options)
    if choice == 1:
        return True
    else:
        return False
    
def create_product_data():
  count = 0
  product_data = []
  for item in data:
      if count == 16:
          break
      count += 1
      item_sub_data = {}
      item_sub_data['pk'] = count
      item_sub_data['model'] = 'store.Product'
      item_sub_data['fields'] = {}
      item_sub_data['fields']['name'] = item['name'][:10]
      item_sub_data['fields']['price'] = item['actual_price'].replace('\u20b9', '').replace(',','.')
      item_sub_data['fields']['description'] = item['name'][:30]
      item_sub_data['fields']['image'] = f'/uploads/products/{str(count)}.png'
      item_sub_data['fields']['category'] = 2
      item_sub_data['fields']['is_sale'] = get_sale_option()
      item_sub_data['fields']['sale_price'] = item['discount_price'].replace('\u20b9', '').replace(',','.')
      product_data.append(item_sub_data)

  #print(product_data)

  with open(product_json_output_file, 'w') as json_file:
      json.dump(product_data, json_file, indent = 4)

def create_category_data():
    category_list = ['electronics', 'books', 'gadgets', 'kitchen', 'sports']
    category_data = []
    for i in range(5):
        item_sub_data = {}
        item_sub_data['pk'] = i + 1
        item_sub_data['model'] = 'store.Category'
        item_sub_data['fields'] = {}
        item_sub_data['fields']['name'] = category_list[i]
        category_data.append(item_sub_data)
    
    with open(category_json_output_file, 'w') as json_file:
      json.dump(category_data, json_file, indent = 4)

create_product_data()
create_category_data()