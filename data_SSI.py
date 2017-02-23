import csv
f = open('stroke_cd.csv', 'r',encoding='utf-8' ,newline='')
lines = csv.DictReader(f)
user_list = []
temp = []
box = []
index = 0
init = 0 
for row in lines:
	if(temp == [row['fee_ym'],row['appl_type'],row['appl_date'],row['case_type'],row['hosp_id'],row['seq_no']]):
		box.append(row['order_code'])
	else:
		if(init == 0):
			init = init +1
		else:
			user_list.append([temp,box])
		box = []
		temp = [row['fee_ym'],row['appl_type'],row['appl_date'],row['case_type'],row['hosp_id'],row['seq_no']]
		box.append(row['order_code'])
		index = index + 1
user_list.append([temp,box])

print("Process Over")
drug = []
data = open('test.csv', 'r',encoding='utf-8' ,newline='')
lines = csv.DictReader(data)
for row in lines:
	if(row['code']!=" "):
		drug.append(row['code'])

BST = ['13007C','13008B','13012C','13016B','13026C']
ICU = [ '03012G','03010E','03011F']
final_data = []

for data in user_list:
	SSI = 9.6804
	#print(data[1])
	if('47042C' in data[1]):
		SSI = SSI + 3.5083
	if('47014C' in data[1]):
		SSI = SSI + 1.6569
	if('47017C' in data[1]):
		SST = SSI + 4.5809

	ICU_com = [val for val in ICU if val in data[1]]
	BST_com = [val for val in BST if val in data[1]]
	o_com = [val for val in drug if val in data[1]]
	
	if(len(BST_com)!= 0):
		SSI = SSI + 1.3642
	if(len(ICU_com)!= 0):
		SSI = SSI + 4.177
	else:
		SSI = SSI - 5.5761
	if(len(o_com)!= 0 ):
		SSI = SSI + 2.1488
	data[0].append(SSI)
	final_data.append(data[0])
f = open("final_data.csv","w",newline='')
w = csv.writer(f)
w.writerows(final_data)
f.close()