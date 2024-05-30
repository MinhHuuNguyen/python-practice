# Bài tập 2: Nhập điểm trung bình (dtb) của một học sinh từ bàn phím, sau đó in ra màn hình xếp loại của học sinh này. 
# Biết rằng: 
# dtb < 4: Xếp loại yếu 
# 4 <= dtb < 6.5: Xếp loại trung bình 
# 6.5 <= dtb < 8: Xếp loại khá 
# dtb >= 8: Xếp loại giỏi 

dtb = float(input("Nhập điểm trung bình của học sinh: "))

if dtb < 4:
    print("Xếp loại yếu")
elif 4 <= dtb < 6.5:
    print("Xếp loại trung bình")
elif 6.5 <= dtb < 8:
    print("Xếp loại khá")
else: # dtb >= 8
    print("Xếp loại giỏi")
