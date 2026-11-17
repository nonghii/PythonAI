# Завдання 1
# Напишіть програму для роботи онлайн магазину.
# Товари:
# ● подушка – 650 грн
# ● ковдра – 1700 грн
# ● лампа – 500 грн
# ● брелок – 60 грн
# Меню дій:
# ● додати товар
# ● видалити товар
# ● очистити кошик
# ● показати вміст кошики та суму покупки
# ● вихід
# Користувачу показується меню один раз на початку
# програми
# Користувач вибирає номер дії після чого за потреби
# вводить назву товару то його кількість
# У випадку неправильно введених даних повідомити про
# це та повернутись до вибору номера дії
# Створіть для кожного товару змінну з кількістю цього
# товару у кошику для подальшої роботи

# PILLOW = 0
# BLANKET = 0
# LAMP = 0
# KEYCHAIN = 0
#
# print("ONLINE SHOP")
# print("1. Додати товар")
# print("2. Видалити товар")
# print("3. Очистити кошик")
# print("4. Показати кошик та суму")
# print("5. Вихід")
#
# while True:
#     action = int(input("Оберіть дію: "))
#
#     if action == 1:
#         product = input("Введіть назву товару: ")
#         amount = int(input("Введіть кількість: "))
#
#         if amount <= 0:
#             print("Неправильна кількість!")
#
#         elif product == "подушка":
#             pillow += amount
#
#         elif product == "ковдра":
#             blanket += amount
#
#         elif product == "лампа":
#             lamp += amount
#
#         elif product == "брелок":
#             keychain += amount
#
#         else:
#             print("Такого товару немає")
#
#     elif action == 2:
#         product = input("Введіть назву товару: ")
#         amount = int(input("Введіть кількість: "))
#
#         if product == "подушка" and amount <= pillow and amount > 0:
#             pillow -= amount
#
#         elif product == "ковдра" and amount <= blanket and amount > 0:
#             blanket -= amount
#
#         elif product == "лампа" and amount <= lamp and amount > 0:
#             lamp -= amount
#
#         elif product == "брелок" and amount <= keychain and amount > 0:
#             keychain -= amount
#
#         else:
#             print("Неправильні дані")
#
#     elif action == 3:
#         pillow = 0
#         blanket = 0
#         lamp = 0
#         keychain = 0
#         print("Кошик очищено")
#
#     elif action == 4:
#         total = pillow * 650 + blanket * 1700 + lamp * 500 + keychain * 60
#
#         print("Ваш кошик:")
#         print("Подушка:", pillow)
#         print("Ковдра:", blanket)
#         print("Лампа:", lamp)
#         print("Брелок:", keychain)
#         print("Сума покупки:", total, "грн")
#
#     elif action == 5:
#         print("Дякуємо за покупку!")
#         break
#
#     else:
#         print("Неправильний номер дії")
