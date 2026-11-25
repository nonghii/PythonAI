# Завдання 4
# Створіть нову гілку practice/pizza
# Перейдіть на неї та реалізуйте програму замовлення
# піци в декілька комітів

while True:
    print("1. Вибрати піцу")
    print("2. Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        name = input("Введіть назву піци: ")
        quantity = int(input("Введіть кількість: "))

        print("Замовлено", name, quantity, "шт.")

    elif choice == "2":
        print("Дякуємо за замовлення!")
        break

    else:
        print("Неправильний вибір")
