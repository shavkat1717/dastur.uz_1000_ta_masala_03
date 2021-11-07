A=int(input("Istalgan uch xonali butun sonni kiriting A => "))
import math
a=math.floor(A/100)
if 1<=a<10:
    aq=A-a*100
    b=math.floor(aq/10)
    bq=aq-b*10
    print((b-a>0 and bq-b>0) or (b-a<0 and bq-b<0))
else:
    print("Iltimos uch xonali son kiriting yoki,\nUshbu sonning raqamlari ketma-ket o'sib boruvchi yoki aksincha emas")