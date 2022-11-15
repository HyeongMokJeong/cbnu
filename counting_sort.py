import time

def arrayPrint(ary):
    print(*ary)

def sort(ary):
    dic = {i : 0 for i in range(100000)}
    result = []

    for i in ary: dic[i] += 1
    
    for i in dic.keys():
        for j in range(dic[i]):
            result.append(i)
    
    return result

def readFile(name):
    f = open(name, "r")

    data = f.readline()
    ary = list(map(int, data.split(', ')))
    f.close()
    
    return ary

ary = readFile("test.txt")
start = time.time()
arrayPrint(sort(ary))
print("time: ", time.time() - start)