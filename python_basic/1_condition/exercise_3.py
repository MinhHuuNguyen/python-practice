# Bài tập 3: Nhập vào lần lượt 3 hệ số a, b, c của phương trình bậc 2 (ax^2+bx+c = 0). Giải phương trình bậc 2 trên và in nghiệm ra màn hình. 

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải phương trình bậc 2")
else: # a != 0
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép x = {x}")
    else: # delta > 0
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
