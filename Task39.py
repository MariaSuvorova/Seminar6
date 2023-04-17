
n = int(input())
numbers_n = input().split()
numbers_n = [int(numbers_n[i]) for i in range(n)]

m = int(input())
numbers_m = input().split()
numbers_m = [int(numbers_m[i]) for i in range(m)]

dif_num = list()
for i in numbers_n:
    if i not in numbers_m:
        dif_num.append(i)
print(*dif_num)
