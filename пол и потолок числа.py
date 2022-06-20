Пол и потолок
Напишите программу, вычисляющую значение \lceil x\rceil + \lfloor x\rfloor⌈x⌉ +⌊x⌋ по заданному вещественному числу xx.

Формат входных данных
На вход программе подается одно вещественное число xx.

Формат выходных данных
Программа должна вывести одно число – значение указанного выражения.

Примечание. \lceil x\rceil⌈x⌉ – потолок числа, \lfloor x\rfloor⌊x⌋ – пол числа.

Тестовые данные 🟢
Sample Input 1:

5.5
Sample Output 1:

11
Sample Input 2:

5.4
Sample Output 2:

11
Sample Input 3:

-12.2
Sample Output 3:

-25

from math import * 
x = float(input())
print(ceil(x) + floor(x))
