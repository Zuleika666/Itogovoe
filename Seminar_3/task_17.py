# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

list = [random.randint(-5, 5) for i in range(int(input("Введите длину массива:  ")))]
list_2 = []

for i in list:
    if i not in list_2:
        list_2.append(i)
       
print(list, list_2)        