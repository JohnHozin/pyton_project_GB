#  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

for i in [True, False]:
    for j in [True, False]:
        for k in [True, False]:
            print(f'X = {i}, Y = {j}, Z = {k} => {not (i or j or k) == (not i and not j and not k)}')