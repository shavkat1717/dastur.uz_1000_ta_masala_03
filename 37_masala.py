x1=int(input("Shaxmatning x1 koordinatasini kiriting: x1 => "))
y1=int(input("Shaxmatning y1 koordinatasini kiriting: y1 => "))
x2=int(input("Shaxmatning x2 koordinatasini kiriting: x2 => "))
y2=int(input("Shaxmatning y2 koordinatasini kiriting: y2 => "))
if ((1<=x1<=8 and 1<=y1<=8) or (1<=x2<=8 and 1<=y2<=8)):
    print(-1<=x1-x2<=1 and -1<=y1-y2<=1)
else:
    print("Shaxmatning koordinatasi [1;8] oralig'ida yotishi kerak.")