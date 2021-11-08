import math
a=math.fabs(float(input("Uchburchakning a tomonini kiriting: a => ")))
b=math.fabs(float(input("Uchburchakning b tomonini kiriting: b => ")))
c=math.fabs(float(input("Uchburchakning c tomonini kiriting: c => ")))
print((a**2+b**2==c**2) or (a**2+c**2==b**2) or (c**2+b**2==a**2))