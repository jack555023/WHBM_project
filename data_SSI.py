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

for data in user_list:
	SSI = 9.6804
	#print(data[1])
	if('47042C' in data[1]):
		SSI = SSI + 3.5083
	if('47014C' in data[1]):
		SSI = SSI + 1.6569

	BST_com = [val for val in BST if val in data[1]]
	ICU_com = [val for val in ICU if val in data[1]]
)