# отсортировать по алфавиту и познакомить парней и девушек

boys = ['Петя', 'Саша', 'Женя', 'Артур', 'Рома', 'Влад']
girls = ['Катя', 'Лиза', 'Кира', 'Яна', 'Кристина', 'Вера']

boys.sort()
girls.sort()
dating = zip(boys, girls)
if len(boys) == len(girls):
    for i, j in dating:
        print(f'{i} и {j}')
else:
    print("Кто-то останется без пары!")
