Сумма делителей
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет сумму всех его делителей.

Входные данные
На вход программе подается натуральное число nn.

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Функция подсчета суммы всех делителей числа является очень важной в теории чисел.

Тестовые данные 🟢
Sample Input 1:

10
Sample Output 1:

18
Sample Input 2:

50
Sample Output 2:

93
Sample Input 3:

3
Sample Output 3:

4



n = int(input())
counter = 0
for i in range(1, n+1):
    if n % i == 0:
        counter += i
print(counter)
        
        