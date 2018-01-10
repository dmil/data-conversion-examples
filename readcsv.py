import csv
from pprint import pprint

with open('fruitcosts.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

for item in rows:
	print(item['fruit'])
