from statistics import mode
import model_sub as model
import view
import logger as log

def button_click():
    value_a = view.get_value()
    log.temperature_logger(value_a)
    value_b = view.get_value()
    log.temperature_logger(value_b)
    model.init(value_a, value_b)
    result = model.do_it()
    log.temperature_logger(result)
    view.view_data(result, "result")
