a = int(input("Nhap so nguyen: "))
if a % 3 == 0 and a % 5 == 0:
    print("a chia het cho 3 va 5")
elif a % 3 == 0 and a % 5 != 0:
    print("a chia het cho 3 nhung khong chia het cho 5")
elif a % 5 == 0 and a % 3 != 0:
    print("a chia het cho 5 nhung khong chia het cho 3")
else:
    print("a khong chia het cho 3 va 5")