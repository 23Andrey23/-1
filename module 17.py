#ЧЕРНОВАЯ ФУНКЦИЯ ПРИЛОЖЕНИЯ БАНКА
#КАЖДОЕ ВВЕДЕННОЕ ЧИСЛО ЧЕРЕЗ ПРОБЕЛ В СПИСКЕ, ЭТО СРЕДСТВА КОТОРЫЕ ХРАНЯТСЯ НА СБЕРЕГАТЕЛЬНОМ СЧЕТЕ(id)
mas = list(map(int, input('Сберегательные средства:').split()))
n = len(mas)


def sorting(mas):
    for q in range(len(mas)-1):
        for i in range(len(mas)-1):
            if mas[i] > mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
    return mas
print(sorting(mas))


def remove():
    while True:
        try:
            rem = int(input("Введите точную сумму денежных средств, которые хранятся на сберегательном счете и этот счет заблоктруется:"))
            if rem in mas:
                mas.remove(rem)
                print(f'Результат {mas}')
                break
            elif rem is not mas:
                print('Сумму которую вы ввели нет в указанном списке')
                remove()
                break
        except ValueError as error:
            print('Вводить можно только числа')


def add():
    while True:
        try:
            add = int(input("Введите сумму которые вы хотите положить на новый сберегательный счет:"))
            if add <= 0:
                print('Чтобы открыть счет вы должны внести деньги')
            elif add in mas or add is not mas:
                mas.append(add)
                print(f'Ваш новый сберегательный счет:{add}')
                print(f'Ваши счита {mas}')
                break
        except ValueError as error:
            print('Вводить можно только числа')


def item_number():
    try:
        number = int(input('Введите точную сумму денежных средств которые хранятся на счете и вы узнаете номер этого счета:'))
        low = 0
        high = n - 1
        middle = (low + high) // 2
        while number != mas[middle] and low < high:
            if number > mas[middle]:
                low = middle + 1
            else:
                high = middle - 1
            middle = (low + high) // 2
        if number == mas[middle]:
            print(f'Номер счета-{middle}')
        elif number > mas[middle]:
            print('Сумму которые вы ввели нет в списке')
        elif number < 0:
            print("Сумму которые вы ввели нет в списке")
            item_number()
    except ValueError as error:
        print('Вводить можно только числа')
        item_number()


while True:
    a = input(('Введите команду "remove", если хотите заблокировать номер сберегательного счета;\nВведите команду "add", если хотите добавить новый сберегательный счет;\nВведите команду "account", если хотите узнать номер счета на котором лежат деньги.\nПоле для ввода:'))
    if a == "remove":
        remove()
    elif a == "add":
        add()
    elif a == "account":
        item_number()
    else:
        print("Вы неправильно ввели команду, попробуйте еще раз")