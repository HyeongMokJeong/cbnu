def base2(num, result): # num은 10진수, result는 결과값
    if num // 2 < 2:
        return (str(num // 2) + str(num % 2) + result)
    else: 
        return base2(num // 2, (str(num % 2) + result))
    
def base8(num, result):
    if num // 8 < 8:
        return (str(num // 8) + str(num % 8) + result)
    else: 
        return base2(num // 8, (str(num % 8) + result))

def base16(num, result):
    if num // 16 < 16:
        if num // 16 == 0:
            de_result = format((num % 16), 'x') + result
        else: de_result = format((num // 16), 'x') + format((num % 16), 'x') + result
        return de_result
    else:
        print(format(num % 16))
        return base2(num // 16, (format(num % 16), 'x') + result)

input_num = int(input("10진수를 입력 --> "))
print()
print("2진수 : " + base2(input_num, ''))
print("8진수 : " + base8(input_num, ''))
print("16진수 : " + base16(input_num, ''))