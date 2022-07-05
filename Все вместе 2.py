Все вместе 2
Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

Тестовые данные 🟢
Sample Input 1:

56639
Sample Output 1:

1
1
2
21
9
1
Sample Input 2:

56689932106
Sample Output 2:

1
3
6
44
648
2
Sample Input 3:

255
Sample Output 3:

0
2
1
0
1
2




n = int(input())
count3 = 0
countLast = 0
countChet = 0
sumBig5 = 0
multyBig7 = 1
count05 = 0
last = n % 10
while n > 0:
    x = n % 10
    if x == 3:
        count3 += 1
    if x == last:
        countLast += 1
    if x % 2 == 0:
        countChet += 1
    if x > 5:
        sumBig5 += x
    if x > 7:
        multyBig7 *= x
    if x == 0 or x == 5:
        count05 += 1
    n //= 10
print(count3)
print(countLast)
print(countChet)
print(sumBig5)
print(multyBig7)
print(count05)