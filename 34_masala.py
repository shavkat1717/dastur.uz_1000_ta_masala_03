x=int(input("Shaxmatning x koordinatasini kiriting: x => "))
y=int(input("Shaxmatning y koordinatasini kiriting: y => "))
if (1<=x<=8 and 1<=y<=8):
    print(x%2==0 and y%2!=0)
else:
    print("Shaxmatning koordinatasi [1;8] oralig'ida yotishi kerak.")