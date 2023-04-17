
n = int(input())
numbers1 = input().split()
numbers1 = [int(numbers1[i]) for i in range(n)]

m = int(input())
numbers2 = input().split()
numbers2 = [int(numbers2[i]) for i in range(m)]

dif_num = list()
for i in numbers1:
    if i not in numbers2:
        dif_num.append(i)
print(*dif_num)
