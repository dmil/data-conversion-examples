vegetables = [
 {'name': 'eggplant'},
 {'name': 'tomato'},
 {'name': 'corn'},
 {'name': 'tomato'},
 {'name': 'corn'},
 {'name': 'tomato'},
 {'name': 'corn'},
 {'name': 'kale'},
 {'name': 'kale'},
 {'name': 'squash'},
]

import csv

with open('veggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'length'])
    for veggie in vegetables:
        # i want the name of the vegetable
        vegetable_name = veggie['name']
        # i want the length of that word
        veggie_name_length = len(veggie['name'])
        # Write those to CSV
        row = [vegetable_name, veggie_name_length]
        writer.writerow(row)