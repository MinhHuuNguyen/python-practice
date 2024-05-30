# Câu 4: Tạo 1 danh sách có 5 số. Sau đó tạo 2 biến x, y lưu trữ 2 số được nhập vào từ bàn phím.
# Chèn x vào vị trí thứ 2 trong danh sách, y vào trị trí cuối cùng trong danh sách. 

x = input('Nhap so x: ')
y = input('Nhap so y: ')

x = float(x)
y = float(y)

my_list = [15, 4, 97, 79, 88]

print('List truoc khi chinh sua:', my_list)

my_list.insert(2, x)
my_list.append(y)

print('List sau khi chinh sua:', my_list)
