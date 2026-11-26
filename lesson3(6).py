# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть
# результат

# numbers = [1, 8, -5, 9]
#
# print(numbers)
#
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 3
#
# print(numbers)
#
# for i in range(len(numbers)):
#     if numbers[i] > 10:
#         numbers[i] = 0
#
# print(numbers)

# Завдання 2
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

# numbers = []
#
# while True:
#     number = int(input("Введіть число (поки не введете -1: "))
#
#     if number == -1:
#         break
#
#     numbers.append(number)
#
# print("Кількість:", len(numbers))
# print("Сума:", sum(numbers))
# print("Мінімальне:", min(numbers))
# print("Максимальне:", max(numbers))
# print("Середнє:", sum(numbers) / len(numbers))

# Завдання 3
# Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді

# positive = []
# negative = []
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#
#     if number == 0:
#         break
#
#     if number > 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)

# Завдання 4
# Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба
# збільшити усім зарплату.
# Виведіть нові зарплати

# salaries = []
# while True:
#     salary = int(input("Введіть зарплату (-1 для завершення): "))
#
#     if salary == -1:
#         break
#
#     salaries.append(salary)
#
# percent = int(input("Введіть відсоток збільшення: "))
#
# for i in range(len(salaries)):
#     salaries[i] = salaries[i] + salaries[i] * percent / 100
# print("Нові зарплати:", salaries)

# Завдання 5
# Користувач вводить кількість днів, після чого
# температуру повітря кожного дня.
# Збережіть температури у список
# Для кожного дня порахуйте різницю температур з
# попереднім днем.
# Виправіть помилку в коді


# days = int(input("Введіть кількість днів: "))
# temperatures = []
# for i in range(days):
#
#     temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#     temperatures.append(temperature)
#
# print("Температури:", temperatures)
#
# for i in range(1, days):
#     difference = temperatures[i] - temperatures[i - 1]
#     print(f"Різниця температур за {i + 1}-й день: {difference}")
