code:
n = input()
s = 0
while n > 10:
    if n % 2 == 1:
        s = n % 10
    n //= 10
print(s)


my review:
n = int(input())
s = 0
last_digit = 0
while n > 0:
    last_digit = n % 10
    if last_digit % 2 == 0:
        s += last_digit
    n //= 10
print(s)