#1
spisok = [1, "one", 1.0, [1, 2, 3], (1, 3, 6), {1, 4, 5}, {"word": 1, "number": 3},
          None, True, False, ValueError]

for element in spisok:
    print(type(element))

#2
text = input("введите что хотите через пробел: ")
spisok_x = text.split()
for index in range(0, len(spisok_x) - 1, 2):
    spisok_x[index], spisok_x[index+1] = spisok_x[index+1], spisok_x[index]
print(spisok_x)