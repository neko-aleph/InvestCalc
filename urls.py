from flask import Blueprint, render_template, request

import calculator

urls_blueprint = Blueprint('urls', __name__,)


@urls_blueprint.route('/')
def hello_world() -> render_template:
    return render_template('index.html')


@urls_blueprint.route('/calculate', methods=['POST'])
def calculate() -> render_template:
    data: dict[str, str] = request.form

    try:
        start_capital: float = float(data['startCapital'])
        interest: float = float(data['interest']) * .01
        months: int = int(data['period']) * int(data['periodUnits'])
        reinvest_period: int = int(data['reinvestPeriod'])
    except ValueError:
        return render_template('error.html', error='Некорректные входные данные')

    result: list[dict[str, str]] = calculator.calculate(start_capital, interest, months, reinvest_period)

    return render_template('result.html', months=result)
