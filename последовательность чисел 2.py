Последовательность чисел 3 🌶️
Даны два целых числа mm и nn (m > nm>n). Напишите программу, которая выводит все нечетные числа от mm до nn включительно в порядке убывания.

Формат входных данных
На вход программе подаются два целых числа mm и nn, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести числа в соответствии с условием задачи.

Примечание. Попробуйте решить задачу двумя способами: с использованием условного оператора if и без него.

Тестовые данные 🟢
Sample Input 1:

77
62
Sample Output 1:

77
75
73
71
69
67
65
63
Sample Input 2:

6
-2
Sample Output 2:

5
3
1
-1
Sample Input 3:

9980
9972
Sample Output 3:

9979
9977
9975
9973


# put your python code here
m, n = int(input()), int(input())
for i in range((m%2+m-1), n-1, -2):
    print(i)