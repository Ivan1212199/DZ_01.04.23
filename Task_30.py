"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
"""

a1= int(input("Введите значение первого элемента: "))
d=int(input("Введите разность элементов: "))
n=int(input("Введите количество элементов: "))
result = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(result)