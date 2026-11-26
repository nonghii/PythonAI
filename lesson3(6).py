# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть
# результат

numbers = [1, 8, -5, 9]

print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 3

print(numbers)

for i in range(len(numbers)):
    if numbers[i] > 10:
        numbers[i] = 0

print(numbers)
