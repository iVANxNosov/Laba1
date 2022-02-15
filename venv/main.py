import math

a=int(input())
b=int(input())
c=int(input())

D = b*b-4*a*c
print("Дискриминант", D)

if D>0:
    x1 = (-b+math.sqrt(D)) / (2*a)
    x2 = (-b-math.sqrt(D)) / (2*a)
    print(x1, x2)
elif D==0:
    x = -b / (2*a)
    print(x)
else:
    print("Корней нет")
