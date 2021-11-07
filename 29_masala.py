import math
x=math.fabs(int(input("Nuqtaning absissa o'qidagi koordinatasini kiriting: x => ")))
y=math.fabs(int(input("Nuqtaning ordinata o'qidagi koordinatasini kiriting y => ")))
x1=math.fabs(int(input("TTning chap yuqori uchi absissalar o'qidagi koordinatasini kiriting: x1 => ")))
y1=math.fabs(int(input("TTning chap yuqori uchi ordinatalar o'qidagi koordinatasini kiriting y1 => ")))
x2=math.fabs(int(input("TTning o'ng pastki uchi absissalar o'qidagi koordinatasini kiriting: x2 => ")))
y2=math.fabs(int(input("TTning o'ng pastki uchi ordinatalar o'qidagi koordinatani kiriting y2 => ")))
print(x1<x<x2 and y2<y<y1)