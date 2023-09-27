import math
a = int 

while ( a != 11 ):
 print ("Выберите операцию")
 print ("1.Сложение")
 print ("2.Вычитание")
 print ("3.Умножение")
 print ("4.Деление")
 print ("5.Возведение в степень")
 print ("6.Квадратный корень")
 print ("7.Факториал")
 print ("8.Синус")
 print ("9.Косинус")
 print ("10.Тангенс")
 print ("11.Выйти из программы")

 a = int (input())

 if a == 1:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        c = int(input("Введите 2 число: "))
        print ("результат:", b + c)
        break
    except ValueError:
        print("Символ вводить нельзя, введите число") 
 elif a == 2:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        c = int(input("Введите 2 число: "))
        print ("результат:", b - c)
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
 elif a == 3:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        c = int(input("Введите 2 число: "))
        print ("результат:", b * c)
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
 elif a == 4:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        c = int(input("Введите 2 число: "))
        if c != 0: 
         print ("результат:", b / c)
        else:
         print ("делить на ноль нельзя")
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
 elif a == 5:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        c = int(input("Введите 2 число: "))
        print ("результат:", b ** c)
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
 elif a == 6:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        if b < 0: print ("недопустимое значение")
        else: print ("результат:", math.sqrt(b))
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
 elif a == 7:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        if b < 0: print ("недопустимое значение")
        else: print ("результат:", math.factorial(b))
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
 elif a == 8:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        print ("результат:", math.sin(b))
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
 elif a == 9:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        if a == 5: print ("результат:", math.cos(b))
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
 elif a == 10:
  while True:
    try:
        b = int(input("Введите 1 число: "))
        if a == 5: print ("результат:", math.tan(b))
        break
    except ValueError:
        print("Символ вводить нельзя, введите число")
