# Câu 2: Tạo 2 biến a và b. Yêu cầu người dùng nhập vào từ bàn phím 2 số ngẫu nhiên.
# Kiểm tra a có chia hết cho b hay không? 
# Nếu có, in ra màn hình dòng chữ “a chia het cho b”
# Ngược lại, in ra dòng chữ “ a khong chia het cho b” (nhập b khác 0)

a = input('Nhap so a: ')
b = input('Nhap so b: ')

a = int(a)
b = int(b)

if b == 0:
    print('Khong the chia cho 0')
else: # b != 0
    if a % b == 0:
        print('a chia het cho b')
    else: # a % b != 0
        print('a khong chia het cho b')

