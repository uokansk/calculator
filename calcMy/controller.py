import re

import calcMy
import view


def button_click():
    nums = re.findall(r'\d*\.\d+|\d+|\S', view.get_value())
    value_a = nums[0]
    value_b = nums[2]
    value_sign = nums[1]
    calcMy.init(value_a, value_b, value_sign)
    result = calcMy.complete()
    view.view_data(result)
