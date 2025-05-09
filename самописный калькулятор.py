Самописный калькулятор 🌶️
Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция». Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

Формат входных данных
На вход программе подаются два целых числа, каждое на отдельной строке, и строка.

Формат выходных данных
Программа должна вывести результат применения операции к введенным числам или соответствующий текст, если операция неверная либо если происходит деление на ноль.

Тестовые данные 🟢
Sample Input 1:

6104
0
/
Sample Output 1:

На ноль делить нельзя!
Sample Input 2:

25
5
*
Sample Output 2:

125
Sample Input 3:

89
80
-
Sample Output 3:

9
Sample Input 4:

567
433
+
Sample Output 4:

1000




x = int(input())
y = int(input())
z = input()
if z == "+":
    print(x + y)
elif z == '/':
    if y == 0: 
        print('На ноль делить нельзя!')
    else: print(x / y)
elif z == "-":
    print(x - y)
elif z == "*":
    print(x * y)
elif z == '/':
    if y == 0: 
        print('На ноль делить нельзя!')
    else: print(x / y)
elif (z != x + y or z != x * y or z != x - y or z != x / y):
    print('Неверная операция')