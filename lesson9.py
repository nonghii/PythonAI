# Завдання 1
# Користувач вводить число від 1 до 9. Потрібно вивести
# для цього числа таблицю множення.
# Наприклад для 5 це буде:
# 1х5=5
# 2х5=10
# …
# 9х5=45
# 10х5=50
# Якщо користувач ввів неправильне число то
# продовжувати запитувати поки не введе правильне.


# while True:
#     number = int(input("Введіть число від 1 до 9: "))
#
#     if number >= 1 and number <= 9:
#         break
#
#     print("Неправильне число. Спробуйте ще раз.")
#
# for multiplier in range(1, 11):
#     result = multiplier * number
#     print(f"{multiplier} x {number} = {result}")


# Завдання 2
# Користувач вводить свої оцінки поки не введе 0. Після
# чого програма виводить середню оцінку.
# Виправіть помилку в коді

# total = 0
# count = 0
#
# while True:
#     grade = int(input("Введіть оцінку: "))
#
#     if grade == 0:
#         break
#
#     total += grade
#
# average_grade = total / count
# print(f"середня оцінка: {average_grade}")

# Завдання 3
# Напишіть простий калькулятор
# Користувач вводить два числа після чого обирає яку дію
# виконати:
# 1. сума
# 2. різниця
# 3. добуток
# 4. частка
# 5. вихід
# Якщо користувач обрав частку, то переконайтесь що не
# буде ділення на 0. У випадку проблеми виведіть відповідне
# повідомлення.


# while True:
#     operation = int(input("Оберіть дію: 1. сума 2. різниця 3. добуток 4. частка 5. вихід: "))
#
#     if operation == 5:
#         print("Вихід з програми")
#         break
#
#     elif operation == 1 or operation == 2 or operation == 3 or operation == 4:
#         num1 = float(input("Введіть перше число: "))
#         num2 = float(input("Введіть друге число: "))
#
#         if operation == 1:
#             result = num1 + num2
#             print(result)
#
#         elif operation == 2:
#             result = num1 - num2
#             print(result)
#
#         elif operation == 3:
#             result = num1 * num2
#             print(result)
#
#         elif operation == 4:
#             if num2 != 0:
#                 result = num1 / num2
#                 print(result)
#             else:
#                 print("На нуль ділити не можна")
#
#     else:
#         print("Неправильний вибір")

# Завдання 4
# Програма повинна зареєструвати рівно 3 учасників. Для
# цього користувач вводить їхні імена, але ім’я admin уже
# зайняте.
# Виправіть помилку в коді

for i in range(3):
    name = input("Введіть ім'я: ")

    if name == "admin":
        print("Це ім'я недоступне")
    else:
        print(f"Учасник №{i}: {name}")
