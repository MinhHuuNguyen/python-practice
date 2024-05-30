# Câu 3: Tạo biến year yêu cầu người dùng nhập vào 1 số (giả sử người dùng luôn nhập số > 0 ). 
# Hãy kiểm tra year và in ra màn hình năm đó có phải là năm nhuận hay không?

year = input('Nhap nam: ')

if len(year) != 4:
    print('Nam khong hop le')
else:
    year = int(year)

    if year <= 0:
        print('Nam khong hop le')
    else: # year > 0
        if year % 4 == 0:
            print('Nam nhuan')
        else: # year % 4 != 0
            print('Nam khong nhuan')
