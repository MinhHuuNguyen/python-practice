# Bài tập 5: Viết một hàm dem_so_lan_xuat_hien(data) nhận vào một danh sách và đếm số lần xuất hiện của mỗi phần tử trong danh sách đó. 

def dem_so_lan_xuat_hien(data):
    dem = {} # key - value: phần tử - số lần xuất hiện
    for phan_tu in data:
        if phan_tu not in dem:
            dem[phan_tu] = 1
        else:
            dem[phan_tu] += 1
    return dem

data = [1, 2, 3, 4, 4, 5, 5, 5, 5, 5]

print(f"Số lần xuất hiện của các phần tử trong {data} là {dem_so_lan_xuat_hien(data)}")
