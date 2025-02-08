money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Увеличение расходов на 5%

# Переменная для подсчета месяцев
months = 0
expense_percentage=(1-(money_capital/salary)*increase)
# Цикл для подсчета месяцев
while money_capital + salary >= spend:
    # Увеличиваем бюджет за счет зарплаты и подушки безопасности
    budget = money_capital + salary

    # Проверяем, можем ли мы покрыть расходы
    if budget >= spend:
        months += 1
        # Уменьшаем финансовую подушку безопасности
        money_capital -= spend
        # Увеличиваем расходы на 5% для следующего месяца
        spend *= (expense_percentage)

print(f"Количество месяцев, которое можно протянуть без долгов:", months)