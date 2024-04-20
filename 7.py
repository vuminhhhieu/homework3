c1 = float(input("Nhap canh 1: "))
c2 = float(input("Nhap canh 2: "))
c3 = float(input("Nhap canh 3: "))
if c1 + c2 > c3:
    if c1**2 + c2**2 == c3**2:
        print("Day la tam giac vuong")
    elif c1 == c2 == c3:
        print("Day la tam giac deu")
    else:
        print("Day la tam giac binh thuong")
else:
    print("Day khong ohai tam giac")