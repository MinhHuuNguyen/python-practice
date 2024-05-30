# Bài tập 1: Nhập một số nguyên n khác 0 từ bàn phím, kiểm tra xem số n vừa nhập vào đó là số dương hay âm và in ra màn hình

n = int(input("Nhập một số nguyên n khác 0: "))

if n > 0:
    print(f"{n} là số dương")
elif n < 0:
    print(f"{n} là số âm")
else: # n == 0
    print(f"{n} không phải là số dương cũng không phải là số âm")
