print('원문')
text = """ 내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다.
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고 싶다.
우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.
"""

text_list = list(text)
dict = {}
list = [',', '.', ' ', '\n']

for i in range(len(text)):
    if text_list[i] in list: continue
    if text_list[i] not in dict:
        dict[text_list[i]] = 1
    else:
        dict[text_list[i]] +=  1

text_tuple = sorted(dict.items(), key=lambda x: x[1], reverse=True)

print(text)
print("--------------------------\n문자\t빈도수\n--------------------------")
for i in range(len(text_tuple)):
    print(f"{text_tuple[i][0]}\t{text_tuple[i][1]}")