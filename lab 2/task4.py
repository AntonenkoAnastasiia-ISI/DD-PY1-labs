salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

# Переменная для накопления нехватки
total_deficit = 0

# Расчет расходов за каждый месяц
for month in range(months):
    # Если зарплата не покрывает расходы, рассчитываем нехватку
    if spend > salary:
        deficit = spend - salary
        total_deficit += deficit

    # Увеличиваем расходы на 3% для следующего месяца
    spend *= (1 + increase)

# Округляем итоговую нехватку до целого числа
money_capital = round(total_deficit)
print(f"Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", money_capital)