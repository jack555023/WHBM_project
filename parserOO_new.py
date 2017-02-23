import csv
import os
f = open('storke_cd.csv', 'r',encoding='utf-8' ,newline='')
lines = csv.DictReader(f)
for row in lines:
	print(row['fee_ym'])