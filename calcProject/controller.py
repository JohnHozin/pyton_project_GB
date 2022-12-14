import model_complex as model
import view
import logger as log


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_c = view.get_value()
    value_d = view.get_value()
    model.init(value_a, value_b, value_c, value_d)
    log.complex_logger(model.return_x(), "number_1")
    log.complex_logger(model.return_y(), "number_2")
    operation = view.get_operation()
    result = -1
    if operation == "+":
        result = model.do_sum()
        log.complex_logger(result, "addition result")
    elif operation == "-":
        result = model.do_sub()
        log.complex_logger(result, "subtraction result ")
    elif operation == "*":
        result = model.do_mult()
        log.complex_logger(result, "multiplication result")
    elif operation == "/":
        result = model.do_div()
        log.complex_logger(result, "division result")
    else:
        print("Error!")
        log.complex_logger("Error!", "result")
        exit()
    view.view_data(result, "result")
