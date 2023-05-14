import math
print("please enter the parameters (a,b,c)")

a=int(input("Please Enter a: "))

b=int(input("Please Enter b: "))

c=int(input("Please Enter c: "))

delta=math.pow(b,2)-(4*a*c)

if delta==0 :

    x=(-b + math.sqrt(delta))

    print("EQ has no answer,     X=",x)

elif delta<0:

    print("EQ has no answer!")

else :    

    x1=(-b + math.sqrt(delta))/(2*a)

    x2=(-b - math.sqrt(delta))/(2*a)

    print("EQ 2 answer.\n X1= ",x1, "\nX2= " , x2)