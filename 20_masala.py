A=int(input("Istalgan uch xonali butun sonni kiriting A => "))
import math
a=math.floor(A/100)
if 1<=a<10:
    aq=A-a*100
    b=math.floor(aq/10)
    bq=aq-b*10
    print(a-b!=0 and b-bq!=0 and a-bq!=0)
else:
    print("Iltimos! uch xonali son kirit barakatopgur...")