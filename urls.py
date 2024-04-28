from flask import Blueprint, render_template, jsonify, Response, request

urls_blueprint = Blueprint('urls', __name__,)


@urls_blueprint.route('/')
def hello_world() -> render_template:
    return render_template('index.html')


@urls_blueprint.route('/calculate', methods=['POST'])
def calculate() -> render_template:
    data: dict[str, str] = request.form

    start_capital: float = float(data['startCapital'])
    interest: float = float(data['interest']) * .01
    months: int = int(data['period']) * int(data['periodUnits'])
    reinvest_period: int = int(data['reinvestPeriod'])

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

    return render_template('result.html', months=result)
