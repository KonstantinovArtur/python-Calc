import math
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

print ("выберите операцию")
a = int (input ())

while (a !=11):
 while (a < 1):
   if a < 1: print ("недопустимое значение")
   print ("выберите операцию")
 while (a > 11):
  if a > 11: print ("недопустимое значение")
  print ("выберите операцию")
 
 print ("введите 1 число")
 b = int (input ())
 print ("введите 2 число")
 c = int (input ())
 if a == 1: print ("результат:", b + c)
 elif a == 2: print ("Результат:", b - c)
 elif a == 3: print ("результат:", b * c)
 elif a == 4:
    if c != 0: 
     print ("результат:", b / c)
    else:
       print ("делить на ноль нельзя") 
 elif a == 5: print ("результат:", b ** c) 
 elif a == 6: print ("результат:", math.sqrt(b), math.sqrt(c) )
 elif a == 7: 
   if b < 0: print ("недопустимое значение")
   else: print ("результат:", math.factorial(b))
   if c < 0: print ("недопустимое значение")
   else: print ("результат:", math.factorial(c))
 elif a == 8: print("результат:", math.sin(b), math.sin(c))
 elif a == 9: print("результат:", math.cos(b), math.cos(c)) 
 elif a == 10: print("результат:", math.tan(b), math.tan(c))
 print ("выберите операцию")
 a = int (input ())