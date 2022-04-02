train_list = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5), ('토마스', 4), ('헨리', 7), ('토마스', 3), ('에밀리', 8), ('퍼시', 5), ('고든', 13)]

train_list_dic = {}

for i in range(len(train_list)):
    if f"{train_list[i][0]}" in train_list_dic: # 딕셔너리에 항목이 이미 있으면
        value = train_list_dic[train_list[i][0]] + train_list[i][1] # 값은 기존값 + 추가 값
        train_list_dic[train_list[i][0]] = value # 밸류값 변경
    else: # 없으면
        train_list_dic[train_list[i][0]] = train_list[i][1] # 생성

train_list_tuple = sorted(train_list_dic.items(), key=lambda x: x[1], reverse=True) # 튜플화시켜서 정렬
# key는 정렬 기준

print("---------------------------\n기차         총수송량  순위\n---------------------------")
for i in range(len(train_list_tuple)):
    print(f"{train_list_tuple[i][0]}    \t{train_list_tuple[i][1]}", end='')
    if train_list_tuple[i][1] == train_list_tuple[i - 1][1]: # 만약 수송량이 전 사람과 같다면
        print(f"\t{i}")
    else: print(f"\t{(i + 1)}")