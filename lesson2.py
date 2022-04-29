#1
# spisok = [1, "one", 1.0, [1, 2, 3], (1, 3, 6), {1, 4, 5}, {"word": 1, "number": 3},
#           None, True, False, ValueError]
#
# for element in spisok:
#     print(type(element))
#
# #2
# text = input("введите что хотите через пробел: ")
# spisok_x = text.split()
# for index in range(0, len(spisok_x) - 1, 2):
#     spisok_x[index], spisok_x[index+1] = spisok_x[index+1], spisok_x[index]
# print(spisok_x)

#3
data = int(input("введите номер месяц в цыфре от 1 до 12:"))
monthes = [None, "winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"]
print(monthes[data])



# month = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer",
#          9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
# mesyats = int(input("введите ваш месяц в цыфре от 1 до 12:\n"))
# print(month[mesyats])
