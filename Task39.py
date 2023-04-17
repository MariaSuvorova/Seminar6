"""Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод:
7 
3 1 3 4 2 4 12
6
4 15 43 1 15 1
 Вывод: 3 3 2 12"""

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
