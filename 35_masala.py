x1=int(input("Shaxmatning x1 koordinatasini kiriting: x1 => "))
y1=int(input("Shaxmatning y1 koordinatasini kiriting: y1 => "))
x2=int(input("Shaxmatning x2 koordinatasini kiriting: x2 => "))
y2=int(input("Shaxmatning y2 koordinatasini kiriting: y2 => "))
if (1<=x1<=8 and 1<=y1<=8):
    print(((x1%2!=0 and y1%2!=0) or (x1%2==0 and y1%2==0)) and ((x2%2!=0 and y2%2!=0) or (x2%2==0 and y2%2==0)) or ((x1%2!=0 and y1%2==0) or (x1%2==0 and y1%2!=0)) and ((x2%2!=0 and y2%2==0) or (x2%2==0 and y2%2!=0)))
else:
    print("Shaxmatning koordinatasi [1;8] oralig'ida yotishi kerak.")