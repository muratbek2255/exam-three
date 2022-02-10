"""Заполните 2 списка а и b случайными целыми числами и верните 3 / список общих для а и b элементов"""



import random

a = []
b = []

# Проходимся по range и с помощью random выводит разные числа
for i in range(0, 10):
    a.append(random.randint(1, 100))
    b.append(random.randint(1, 100))

result = list(set(a) and set(b))


print(result)


