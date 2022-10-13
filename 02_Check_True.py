# Программа проверяет истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

range = 0,1
for x in range:
    for y in range:
        for z in range:
            if (not(x or y or z)) == (not (x) and not (y) and not (z)):
                print (True)
            else:
                print (False)