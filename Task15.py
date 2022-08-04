# Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.

num = int(input('введите натуральное число n -> '))

def func_factors (num):
    rez = []
    delitel = 2
    while (num != 1):
        if (num % delitel) == 0:
            rez.append(delitel)
            num = num / delitel
        else:
            delitel += 1
    return(rez)

print (func_factors(num))





