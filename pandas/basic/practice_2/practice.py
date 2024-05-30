# Hãy thực hiện các thao tác làm sạch dữ liệu dưới đây:  
# Loại bỏ các giá trị duplicates
# Split dữ liệu trong các cột nếu cột đó chứa nhiều giá trị trong 1 ô
# Xóa khoảng trống ở đầu, cuối hoặc không cần thiết giữa các từ
# Đổi kiểu dữ liệu
# Xử lý các dữ liệu bị thiếu bằng cách drop, thay thế bằng mode, mean, …  

import pandas as pd

# Đọc dữ liệu từ file csv
df = pd.read_csv('data/brasil-real-estate-1.csv')

# Hiển thị của dữ liệu
print(df)

# Duplicates:
# - Giống nhau hoàn toàn: Giống nhau tất cả giá trị trên các cột
# - Giống nhau một phần: Giống nhau một số giá trị trên các cột
# Loại bỏ các giá trị duplicates
df = df.drop_duplicates()
# df = df.drop_duplicates(subset=[])
print(df)

# Split dữ liệu trong các cột nếu cột đó chứa nhiều giá trị trong 1 ô
# Xử lý cột place_with_parent_names
def split_(name):
    return name.split('|')[1:-1]

df['place_with_parent_names'] = df['place_with_parent_names'].apply(split_)
df['number_of_names'] = df['place_with_parent_names'].apply(len)
print(df)
print(df['number_of_names'].value_counts())

df[['place_1', 'place_2', 'place_3', 'place_4']] = pd.DataFrame(df['place_with_parent_names'].tolist(), index=df.index)
print(df)

# Xử lý cột lat-lon
# Xử lý khuyết thiếu:
# - Cách 1: Drop
# - Cách 2: Điền thêm vào:
#     + Cách 2.1: Điền thêm giá trị đặc biệt (-1, -99, 999999 ...)
#     + Cách 2.2: Điền thêm giá trị thống kê (mean, median, mode ...)
df['lat-lon'] = df['lat-lon'].fillna('-999999,-999999')
df[['lat', 'lon']] = df['lat-lon'].str.split(',', expand=True)
print(df)
print(df['lat'].isna().sum())
print(df['lon'].isna().sum())

# Xóa khoảng trống ở đầu, cuối hoặc không cần thiết giữa các từ
df['property_type'] = df['property_type'].str.strip()
df['region'] = df['region'].str.strip()
print(df)

# Đổi kiểu dữ liệu
def process_price_usd(price):
    price = price.replace('$', '')
    price = price.replace(',', '')
    return price

print(df.info())
df['lat'] = df['lat'].astype(float)
df['lon'] = df['lon'].astype(float)
df['price_usd'] = df['price_usd'].apply(process_price_usd)
df['price_usd'] = df['price_usd'].astype(float)
print(df)
print(df.info())

# # Xử lý các dữ liệu bị thiếu bằng cách drop, thay thế bằng mode, mean, …  
# print(df['lat-lon'])
# print(df['lat-lon'].isna().sum())
# df['lat-lon'] = df['lat-lon'].fillna('-999999,-999999')
# df[['lat', 'lon']] = df['lat-lon'].str.split(',', expand=True)
# df['lat'] = df['lat'].astype(float)
# df['lon'] = df['lon'].astype(float)
# # Bước 1: Tính giá trị trung bình
# print(df['lat'])
# lat_value = df['lat']
# lat_value = lat_value[lat_value != -999999]
# print(lat_value)
# print(lat_value.mean())
# # Bước 2: Thay thế giá trị -999999 bằng giá trị trung bình
# df['lat'] = df['lat'].replace(-999999, lat_value.mean())
# print(df['lat'])

