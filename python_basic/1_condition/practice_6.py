# Câu 6: Tạo 3 biến lưu trữ 3 số do người dùng nhập vào từ bàn phím. 
# Kiểm tra xem 3 giá trị vừa nhập phải là độ dài của 1 tam giác hay không?
# (Gợi ý: Sử dụng bất đẳng thức tam giác để làm bài 6)

canh_1 = input('Nhap canh thu nhat: ')
canh_2 = input('Nhap canh thu hai: ')
canh_3 = input('Nhap canh thu ba: ')

canh_1 = float(canh_1)
canh_2 = float(canh_2)
canh_3 = float(canh_3)

print('Do dai 3 canh:', canh_1, canh_2, canh_3)

# Tong cua 2 canh bat ky lon hon canh con lai
# Hieu cua 2 canh bat ky nho hon canh con lai

if (canh_1 + canh_2 > canh_3) and (canh_1 + canh_3 > canh_2) and (canh_2 + canh_3 > canh_1):
    if (abs(canh_1 - canh_2) < canh_3) and (abs(canh_1 - canh_3) < canh_2) and (abs(canh_2 - canh_3) < canh_1):
        print('Ba so', canh_1, canh_2, canh_3, 'tao thanh 1 tam giac')
    else:
        print('Ba so', canh_1, canh_2, canh_3, 'khong tao thanh 1 tam giac')
else:
    print('Ba so', canh_1, canh_2, canh_3, 'khong tao thanh 1 tam giac')
