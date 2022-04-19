#1

# a = 1
# b = 2
# c = 3
# print(a)
# print(a+c)
# age = input("how old are u? ")
# print(age)

#2
# time = int(input("input time in seconds? "))
# hours = time//3600
# minutes = time%3600//60
# seconds = time%3600%60
#
# print(f"{hours:02}:{minutes:02}:{seconds:02}")

#3
#
#x = input("write number n!")
# result = int(x)+int(x*2)+int(x*3)
# print(f"{x}+{x*2}+{x*3}={result}")

#4

number = int(input("get number:"))
biggest = 0
while number > 0:
    tsifra = number % 10
    if tsifra >biggest:
        biggest = tsifra
    number = number // 10
print(F"the biggest number is {biggest}")
