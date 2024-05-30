# Bài tập 5: Tạo 3 biến lưu trữ 3 giá trị nhập vào ngày tháng năm, in ra ngày hôm sau và ngày hôm qua của ngày vừa nhập.

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if nam % 4 != 0 or (nam % 100 == 0 and nam % 400 != 0):
    ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ngay_trong_thang = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= ngay <= 31 and 1 <= thang <= 12 and nam >= 0:
    if 1 <= ngay <= ngay_trong_thang[thang - 1]:
        if ngay < ngay_trong_thang[thang - 1]:
            ngay_hom_sau = ngay + 1
            thang_hom_sau = thang
            nam_hom_sau = nam
        else:
            ngay_hom_sau = 1
            if thang < 12:
                thang_hom_sau = thang + 1
                nam_hom_sau = nam
            else:
                thang_hom_sau = 1
                nam_hom_sau = nam + 1

        if ngay > 1:
            ngay_hom_qua = ngay - 1
            thang_hom_qua = thang
            nam_hom_qua = nam
        else:
            ngay_hom_qua = ngay_trong_thang[thang - 2]
            if thang > 1:
                thang_hom_qua = thang - 1
                nam_hom_qua = nam
            else:
                thang_hom_qua = 12
                nam_hom_qua = nam - 1

        print("Ngày hôm sau là:", ngay_hom_sau, "/", thang_hom_sau, "/", nam_hom_sau)
        print("Ngày hôm qua là:", ngay_hom_qua, "/", thang_hom_qua, "/", nam_hom_qua)
    else:
        print("Ngày không hợp lệ!")
else:
    print("Ngày không hợp lệ!")

