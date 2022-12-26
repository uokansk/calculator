import input
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    input.init(value_a, value_b)
    result = input.summa()
    view.view_data(result)
