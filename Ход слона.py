Ход слона 🌶️
Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.

Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Шахматный слон ходит по диагоналям.
Тестовые данные 🟢
Sample Input 1:

4
4
5
5
Sample Output 1:

YES
Sample Input 2:

4
4
5
4
Sample Output 2:

NO
Sample Input 3:

4
4
5
3
Sample Output 3:

YES


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1-x2)**2 == (y1-y2)**2:
    print('YES')
else:
    print('NO')