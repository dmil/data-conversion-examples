import csv

with open('testwrite.csv', 'w') as f:
    writer = csv.writer(f)

    data = [
    	['col1', 'col2'],
    	['val1', 'val2'],
    	['val1', 'val2'],
    	['val1', 'val2']
    ]

    writer.writerows(data)
