data = ['A37B', '12333', '23CC', '88D9', 'BB8F', '3A9A']
int_data = []

print(f"정렬 전 데이터 --> ", end='')
for i in range(len(data)):
    print(data[i], end=' ')

for i in range(len(data)): # a37b 23cc 88d9
    str_data = ''
    for j in range(len(data[i])): # a 3 7 b
        if data[i][j].isdigit():
            str_data += data[i][j] # '3' + '7' = '37'
        else: continue
    int_data.append(int(str_data))

for i in range(len(int_data) - 1):
    for j in range(i+1, len(int_data)): 
        if int_data[i] > int_data[j]: 
            data[i], data[j], int_data[i], int_data[j] = data[j], data[i], int_data[j], int_data[i]

print("\n정렬 후 데이터 --> ", end='')
for i in range(len(int_data)):
    print(data[i], end=' ')