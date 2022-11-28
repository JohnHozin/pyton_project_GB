colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
# data.writelines(colors)
data.write('LINE 2\n')
data.write('LINE 3\n')
data.close()

exit()

with open('file.txt', 'a') as data:
    data.write('line 1111\n')
    data.write('line 2222\n')

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors)
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


from lections.lection_1 import lec_1
import help as h

print(h.f(2.3))

def new_string(symbol, count=3):
    return symbol * count


print(new_string('!', 5))
print(new_string('!'))
print(new_string(4))

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))
print(concatenatio('a', '1'))

def fib(n):  # Функция Фибоначи
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)

b, c = 3, 4
(a) = (3, 4)  # кортеж
print(a)
print(a[0])
print(a[1])
print(a[-1])

t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')

t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue
t[0] = 'black' # TypeE

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←

print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
     print('{}: {}'.format(item, dictionary[item]))

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)
print()
for e in list2:
    print(e)
list1[0] = 123

for e in list1:
    print(e)
print()
for e in list2:
    print(e)

print(len(list1))
print(list1.pop())
print(list1)

list1.append(23)
list1.insert(2, 11)
print(list1)
