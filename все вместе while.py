Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

Тестовые данные 🟢
Sample Input 1:

5678
Sample Output 1:

26
4
1680
6.5
5
13
Sample Input 2:

132
Sample Output 2:

6
3
6
2.0
1
3
Sample Input 3:

75
Sample Output 3:

12
2
35
6.0
7
12



n,sm,kol,pr = int(input()),0,0,1
np = n % 10
while n != 0:
    sm += n % 10 
    kol +=1
    pr *= n % 10
    n1 = n
    n = n // 10
print(sm,kol,pr,sm/kol,n1,n1+np,sep='\n')