cities = ['Москва', 'Казань', 'Рязань', 'Владимир', 'Тверь', 'Уфа', 'Воронеж', 'Новосибирск']

# уберем заглавные буквы
print(list(map(str.lower, cities)))

# сделаем все буквы заглавными
print(list(map(str.upper, cities)))

# запишем слова задом наперёд
print(list(map(lambda i: i[::-1], cities)))

# оставим только короткие названия
print(list(filter(lambda i: len(i) <= 6, cities)))
