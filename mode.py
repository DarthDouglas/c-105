# Python program to print
# mode of elements
from collections import Counter
import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)



#Calculating Mode
data = Counter(new_data)
print(data)
print(data.items())
mode_data_for_range = {
                        "55-65": 0,
                        "65-75": 0,
                        "75-85": 0
                    }
for height, occurence in data.items():
    if 55 < float(height) < 65:
        mode_data_for_range["55-65"] += occurence
    elif 65 < float(height) < 75:
        mode_data_for_range["60-70"] += occurence
    elif 75 < float(height) < 85:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")
print(mode_data_for_range)
