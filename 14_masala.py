A=int(input("Birinchi butun sonni kiriting A => "))
B=int(input("Ikkinchi butun sonni kiriting B => "))
C=int(input("Ikkinchi butun sonni kiriting C => "))
print((A*B*C>0) and ((A>0 and B<0 and C<0) or (A<0 and B>0 and C<0) or (A<0 and B<0 and C>0)))