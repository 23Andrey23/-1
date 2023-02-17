tickets = int(input("Здравствуйте, при покупку более трех билетов на конференцию вы получаете скидку 10%\n" "Введите количество билетов, которые вы собираетесь приобрести:"))
total = 0
for visitor in range(tickets):
    age = int(input("Возраст поситителя:"))
    if 18 <= age < 25:
        total += 990
        print("Сумма составляет:", total, "рублей")
    elif age < 18:
        print("Бесплатный билет")
    elif age > 25:
        total += 1390
        print("Сумма составляет:", total, "рублей")
if tickets > 3:
    total = total - ((total / 100) * 10)
    print("Со скидкой в 10%, ваша сумма составляет", int(total), "рублей")