# Bài tập 3: Viết một hàm tinh_tong(n) nhận vào một số nguyên dương n và tính tổng các chữ số của n.
# Ví dụ: n = 123, thì hiển thị kết quả là 6.

def tinh_tong(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong

n = int(input("Nhập một số nguyên dương n: "))

print(f"Tổng các chữ số của {n} là {tinh_tong(n)}")
