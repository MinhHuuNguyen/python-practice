# Câu 1: Load bộ dữ liệu Uber và kiểm tra bảng dữ liệu bằng cú pháp head, info : Link
# Câu 2: Định dạng kiểu dữ liệu cột Request ID và Driver ID thành kiểu string
# Câu 3: Định dạng các giá trị nan trong cột Driver ID thành pd. NA ? Sau đó dùng  cú pháp dropna xóa đi các dòng có chứa giá trị NA ?
# Câu 4: Kiểm tra định dạng dữ liệu của các cột Request timetsamp, Drop timestamp ? Viết hàm và xử lý định dạng thời gian đồng nhất cho các cột này ?
# Câu 5: Tạo thêm các cột RequestYear, RequestMonth, DropYear DropMonth  bằng cú pháp datetime.year, datetime.month và định dạnh kiểu dữ liệu integer cho các cột DropYear, DropMonth
# Câu 6: Tạo thêm cột Duration tính khoảng cách thời gian giữa cột Request Timestamp và Drop timestamp, chuyển về dữ liệu dạng phút , định dạng kiểu dư liệu là số thực
# Câu 7: Dùng cú pháp value_counts đếm các giá trị trong các cột “Pickup Point” và cột “Status”
# Câu 8: Vẽ biểu đồ histogram quan sát phân bổ dữ liệu của cột Duration
# Câu 9. Vẽ biểu đồ Boxplot quan sát phân bổ dữ liệu của cột Duration

import pandas as pd

# Câu 1: Load bộ dữ liệu Uber và kiểm tra bảng dữ liệu bằng cú pháp head, info: Link
df = pd.read_csv("data/Uber Request Data.csv")
print(df)
print(df.head())
print(df.info())

# # Câu 2: Định dạng kiểu dữ liệu cột Request ID và Driver ID thành kiểu string
# df['Driver id'] = df['Driver id'].fillna(-99)
# df['Driver id'] = df['Driver id'].astype(int).astype(str)
# df['Request id'] = df['Request id'].astype(str)
# print(df)

# # Câu 3: Định dạng các giá trị nan trong cột Driver ID thành pd. NA?
# # Sau đó dùng cú pháp dropna xóa đi các dòng có chứa giá trị NA?
# print(df['Driver id'])
# df['Driver id'] = df['Driver id'].fillna(pd.NA)
# df = df.dropna(subset=['Driver id'])
# print(df['Driver id'])

# Câu 4: Kiểm tra định dạng dữ liệu của các cột Request timetsamp, Drop timestamp?
# Viết hàm và xử lý định dạng thời gian đồng nhất cho các cột này?
def process_timestamp(timestamp):
    if pd.isnull(timestamp):
        return '2011-11-11 11:11:11'

    day_month_year, hour_min_sec = timestamp.split(' ')
    if '/' in day_month_year: # Type 1: day/month/year
        day, month, year = day_month_year.split('/')
    elif '-' in day_month_year: # Type 2: day-month-year
        day, month, year = day_month_year.split('-')
    else:
        print('Error', day_month_year)
    day = day.zfill(2)
    month = month.zfill(2)
    year = year.zfill(4)

    hour_min_sec_list = hour_min_sec.split(':')
    if len(hour_min_sec_list) == 2: # Type 1: hour:min
        hour, minute = hour_min_sec_list
        second = "00"
    elif len(hour_min_sec_list) == 3: # Type 2: hour:min:
        hour, minute, second = hour_min_sec_list
    else:
        print('Error', hour_min_sec_list)
    hour = hour.zfill(2)
    minute = minute.zfill(2)
    second = second.zfill(2)

    return f'{year}-{month}-{day} {hour}:{minute}:{second}'

# Optional
df = df.dropna(subset=['Request timestamp', 'Drop timestamp'])
df['Request timestamp'] = df['Request timestamp'].apply(process_timestamp)
df['Drop timestamp'] = df['Drop timestamp'].apply(process_timestamp)
print(df)

# Câu 5: Tạo thêm các cột RequestYear, RequestMonth, DropYear DropMonth
# bằng cú pháp datetime.year, datetime.month và định dạnh kiểu dữ liệu integer
# cho các cột DropYear, DropMonth
df['Request timestamp'] = pd.to_datetime(df['Request timestamp'], format='%Y-%m-%d %H:%M:%S')
df['Drop timestamp'] = pd.to_datetime(df['Drop timestamp'], format='%Y-%m-%d %H:%M:%S')

df['RequestYear'] = df['Request timestamp'].apply(lambda x: x.year)
df['RequestMonth'] = df['Request timestamp'].apply(lambda x: x.month)
df['DropYear'] = df['Drop timestamp'].apply(lambda x: x.year)
df['DropMonth'] = df['Drop timestamp'].apply(lambda x: x.month)
print(df)

# Câu 6: Tạo thêm cột Duration tính khoảng cách thời gian giữa cột Request Timestamp và Drop timestamp,
# chuyển về dữ liệu dạng phút, định dạng kiểu dư liệu là số thực
df['Duration'] = (df['Drop timestamp'] - df['Request timestamp']).dt.total_seconds() / 60.0
print(df)

# Câu 7: Dùng cú pháp value_counts đếm các giá trị trong các cột “Pickup Point” và cột “Status”
print(df['Pickup point'].value_counts())
print(df['Status'].value_counts())

# Câu 8: Vẽ biểu đồ histogram quan sát phân bổ dữ liệu của cột Duration
df['Duration'].hist().get_figure().savefig('data/histogram.png')

# Câu 9. Vẽ biểu đồ Boxplot quan sát phân bổ dữ liệu của cột Duration
import matplotlib.pyplot as plt
plt.clf()
df.boxplot(column='Duration').get_figure().savefig('data/boxplot.png')

# Đo độ tương quan
# print(df.corr())
