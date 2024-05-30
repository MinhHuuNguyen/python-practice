# Câu 1: Viết một hàm tinh_tong(n) nhận vào một số nguyên dương n sau đó tính tổng các số từ 1 đến n.

def tinhtong(n):
    if n <= 0:
        print('ko phai so nguyen duong')
    else:
        tong = 0
        for i in range(1, n + 1):
            tong = tong + i
        return tong


n = input('Nhập số n: ')
n = int(n)
tong = tinhtong(n)

print('Tổng các số từ 1 đến', n, 'là:', tong)
