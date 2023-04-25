"""Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:        Вывод:
1 2 3 2 3    2"""

numbers = input().split()
numbers = [int(numbers[i]) for i in range(len(numbers))]
count = 0
while numbers:
    i = numbers[0]
    if numbers.count(i) >= 2:
        count += int(numbers.count(i)//2)
        while i in numbers:
            numbers.remove(i)
    else:
        numbers.remove(i)
print(count)
    