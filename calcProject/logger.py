from datetime import datetime as dt


def complex_logger(data, name):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as file:
        file.write('{}; {}; {}\n'
                   .format(time, name, data))



