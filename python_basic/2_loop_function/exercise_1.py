# Bài tập 1: Viết một hàm kiem_tra_so_nguyen_to(n) nhận vào một số nguyên dương n và kiểm tra xem n có phải là số nguyên tố hay không.
# Sử dụng vòng lặp và kiểm tra các ước số của n để thực hiện tác vụ này.

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    else: # n >= 2
        for i in range(2, int(n / 2 + 1)):
            if n % i == 0:
                return False
        return True

n = int(input("Nhập một số nguyên dương n: "))

if kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")
