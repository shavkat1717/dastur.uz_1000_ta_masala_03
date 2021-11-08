import math
a=math.fabs(float(input("Uchburchakning a tomonini kiriting: a => ")))
b=math.fabs(float(input("Uchburchakning b tomonini kiriting: b => ")))
c=math.fabs(float(input("Uchburchakning c tomonini kiriting: c => ")))
print(a+b>c and (a-b<c or b-a<c)) or (b+c>a and (b-c<a or c-b<a)) or (a+c>b and (a-c<b or c-a<b))