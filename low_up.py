text = list(input("문자열을 입력하세요: "))
for i in range(len(text)):
    j = text[i]
    if (text[i] == j.upper()): # i는 대문자
        text[i] = text[i].lower()
    else:
        text[i] = text[i].upper()
print("대소문자 변환 결과 --> ", end='')
for i in range(len(text)):
    print(text[i], end='')