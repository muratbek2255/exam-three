"""Напишите функцию, которая считает сумму цифр любого целого положительного числа
вход: 459
выход: 18/"""



A = int(input("Введите число: "))
sum = 0

# в цикле while мы генерируем число
while A > 0:
    a = A % 10
    sum += a
    A = A // 10


print(sum)