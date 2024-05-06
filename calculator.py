def calculate(start_capital: float, interest: float, months: int, reinvest_period: int) -> list[dict[str,str]]:
    result: list[dict[str, str]] = list()

    for period in range(1, months + 1):
        if period % (12 // reinvest_period) != 0:
            continue
        month: dict[str, str] = dict()

        amount: float = start_capital * (pow((1 + interest / reinvest_period), reinvest_period * period / 12))
        income: float = amount - start_capital

        month['number'] = f'{period}'
        month['amount'] = f'{amount:.2f}'
        month['income'] = f'{income:.2f}'

        result.append(month)

    return result