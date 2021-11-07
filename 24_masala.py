A=int(input("Istalgan uch xonali butun sonni kiriting A => "))
B=int(input("Istalgan uch xonali butun sonni kiriting B => "))
C=int(input("Istalgan uch xonali butun sonni kiriting C => "))
D=B**2-4*A*C
if A!=0:
    print(D>=0)
else:
    print("Diqqatli bo'ling! A nolga teng bo'lmasin.")