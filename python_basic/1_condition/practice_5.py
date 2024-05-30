# Câu 5: Tạo biến s lưu trữ kết quả mà người dùng nhập vào từ bàn phím.
# Kiểm tra xem trong s các ký tự đặc biệt không? 
# Nếu có, in ra màn hình dòng chữ ‘Yes’, ngược lại in ra dòng chữ ‘No’,
# biết rằng, ký tự đặc biệt là các ký tự !, @, #, $, ^ 

a = input('Nhap chuoi ky tu a: ')

print('Chuoi ky tu a: ', a)

if '!' in a or '@' in a or '#' in a or '$' in a or '^' in a:
    print('Chuoi ky tu a chua cac ky tu dac biet')
    # TODO: In ra man hinh ky tu dac biet nao ma chuoi ky tu a chua
else:
    print('Chuoi ky tu a khong chua cac ky tu dac biet')
