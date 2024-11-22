money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0  # Cколько месяцев можно протянуть без долгов
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while True:
    a = spend - salary
    if a > money_capital:
        break
    months += 1
    money_capital -= a
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", months)
