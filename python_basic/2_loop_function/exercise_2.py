# Bài tập 2: Viết một hàm tinh_giai_thua(n) nhận vào một số nguyên dương n và tính giai thừa của n (n!)

def tinh_giai_thua(n):
    if n == 0:
        return 1
    else:
        giai_thua = 1
        for i in range(1, n + 1):
            giai_thua *= i
        return giai_thua

n = int(input("Nhập một số nguyên dương n: "))

print(f"{n}! = {tinh_giai_thua(n)}")
