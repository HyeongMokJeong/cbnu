 # 선택 정렬 방식으로 16진수 리스트 오름차순 정렬

def ox_sort(list):
    for i in range(len(list) - 1): # 0이라면 1,2,3,4와 비교 / 1이라면 2,3,4와 비교 / 3이라면 4와 비교 / 4라면 비교 x
        # i는 0 1 2 3
        for j in range(i + 1, len(list)):
            # i가 0일때 1 2 3 4 / 1일때 2 3 4 / 2일때 3 4 / 3일때 4
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return

if __name__ == '__main__':
    num_list = [0xA37B, 0x23CC, 0x88D9, 0xBB8F, 0x3A9A]
    num_print_list = list(map(hex, num_list)) # hex는 정수값을 16진수로 변환
    ox_sort(num_list)
    num_print_list_sorted = list(map(hex, num_list))

    print("정렬 전 데이터 : ", end ='')
    for i in range(len(num_print_list)):
        print(f"{num_print_list[i]}", end=' ')
    print("\n정렬 후 데이터 : ", end='')
    for i in range(len(num_print_list_sorted)):
        print(f"{num_print_list_sorted[i]}", end=' ')