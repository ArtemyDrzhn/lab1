import random

a = random.randint(1, 100)
number = int(input("Введите число: "))
while number != a:
    if a > number:
        print(f"Загаданное число больше, чем {number}")
    else:
        print(f"Загаданное число меньше, чем {number}")
    number = int(input("Введите число: "))
else:
    print(f"Угадали! Действительно было загадано число {a}")
