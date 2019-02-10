from PIL import Image, ImageEnhance, ImageFilter
from pytesseract import image_to_string
import re
import json
import requests


# img = Image.open('receipt1.jpg')
# text = image_to_string(img).lower()
# items_string = re.search(pattern = 'daily\n\n([\w\W]*)\n\nsubtotal', string = text).group(1)
# items_list = re.split('[^\n]\n', items_string)
# trimmed_items_list = [re.sub(r'\w\-', '', x) for x in items_list]

# trimmed_items_list = [x for x in trimmed_items_list if '\n' not in x]


# print(trimmed_items_list)

def get_key(keyfile):
	with open(keyfile) as f:
		app_id = f.readline()
		app_key = f.readline()
	return {'app_id': app_id, 'app_key': app_key}

keys = get_key('./keys.txt')
app_id = keys['app_id']
app_key = keys['app_key']



###  nutritionix api stuff

url_template = 'https://trackapi.nutritionix.com/v2/search/item?nix_item_id=513fc9e73fe3ffd40300109f'
r = requests.get(url_template, params = {'x-app-id': app_id, 'x-app-key': app_key})
r.raise_for_status()
