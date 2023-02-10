money = int(input("Money:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
procent = list(per_cent.values())
bank_ТКБ = round(procent[0] / 100 * money)
bank_СКБ = round(procent[1] / 100 * money)
bank_ВТБ = round(procent[2] / 100 * money)
bank_СБЕР = round(procent[3] / 100 * money)
deposit = [bank_ТКБ, bank_СКБ, bank_ВТБ, bank_СБЕР]
print("Накопленные средства за год вклада в каждом из банков —", deposit)
print("Максимальная сумма, которую вы можете заработать —", deposit[1])