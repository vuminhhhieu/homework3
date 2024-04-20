import math
def check_prime_number(n):
    flag = 1;
    if (math.ceil(n) != math.floor(n)):
        flag = 0;
    return flag;      
n = float(input("Nhap vao so thuc: "))
check = check_prime_number(n)
if check == 1:
    print("a la so nguyen")
else:
    print("a la so thuc")