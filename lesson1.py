#1

a = 1
b = 2
c = 3
print(a)
print(a+c)
age = input("how old are u? ")
print(age)

#2
time = int(input("input time in seconds? "))
hours = time//3600
minutes = time%3600//60
seconds = time%3600%60

print(f"clock_time = {hours:02}:{minutes:02}:{seconds:02}")