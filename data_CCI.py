import csv
f = open('CCI.csv', 'r',encoding='utf-8' ,newline='')
lines = csv.DictReader(f)
for row in lines:
	print(row['age'])
