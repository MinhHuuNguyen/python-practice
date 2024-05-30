# Bài tập 4: Viết một hàm tinh_trung_binh(data) nhận vào một danh sách số và tính trung bình cộng của các số trong danh sách đó.
# Sử dụng vòng lặp để lặp qua từng số trong danh sách và tính tổng các số

def tinh_trung_binh(data):
    tong = 0
    for so in data:
        tong += so
    return tong / len(data)

data = [1, 2, 3, 4, 5]

print(f"Trung bình cộng của {data} là {tinh_trung_binh(data)}")
