# Алгоритм перемешивания списка
import time
import random


def random_method(minimum=0, maximum=10):  # алгоритм нахождения случайного числа в интервале (0, 1)
    t = time.time()
    # return int((time.time() % 1) * (maximum - minimum) + minimum)
    time.sleep(0.001)
    return int(round((t % 1 * 10 ** 6) % 1, 1) * (maximum - minimum) + minimum)


num_list = [2, 4, 6]
# random.shuffle(num_list) # перемешивание списка
print(num_list)

for i in range(len(num_list)):
    j = random_method(0, len(num_list) - 1)
    num_list[i], num_list[j] = num_list[j], num_list[i]
print(num_list)

