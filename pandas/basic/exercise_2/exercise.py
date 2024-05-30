# Bài tập 1: Hãy tiến hành xử lý, làm sạch bộ dữ liệu Top 50 Animation Movies and TV Show
# và EDA để tìm ra các thông tin sau của bộ dữ liệu:
# A. Thời lượng trung bình, số votes trung bình của các bộ phim theo từng thể loại
# B. Ratings trung bình của các thể loại là bao nhiêu?
# (gợi ý: tất cả đều có thể loại là animation nên ta có thể bỏ qua animation, chỉ quan tâm 2 thể loại sau)

import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('data/Top 50 Animation Movies and TV Shows.csv')

# Hiển thị thông tin của dữ liệu
print(df)

# Hiển thị các cột của dữ liệu
print(df.columns)

# Tiền xử lý dữ liệu
# Trích xuất dữ liệu thời lượng từ cột Minutes
print('So luong gia tri khuyet thieu tren cot Minutes', df['Minutes'].isna().sum())
# # Cách 1: Loại bỏ các dòng có giá trị khuyết thiếu trên cột Minutes
# df = df.dropna(subset=['Minutes'])
# df['Minutes'] = df['Minutes'].apply(lambda x: int(x.split()[0]))

# Cách 2: Thay thế giá trị khuyết thiếu trên cột Minutes bằng giá trị trung bình của cột Minutes
df['Minutes'] = df['Minutes'].apply(lambda x: int(x.split()[0]) if type(x) == str else x)
df['Minutes'] = df['Minutes'].fillna(df['Minutes'].dropna().mean())

# Xử lý dữ liệu cột Votes
print('So luong gia tri khuyet thieu tren cot Votes', df['Votes'].isna().sum())
# Cách 1: Loại bỏ các dòng có giá trị khuyết thiếu trên cột Votes
# df = df.dropna(subset=['Votes'])
# df['Votes'] = df['Votes'].apply(lambda x: int(x.replace(',', '')))

# Cách 2: Thay thế giá trị khuyết thiếu trên cột Votes bằng giá trị trung bình của cột Votes
df['Votes'] = df['Votes'].apply(lambda x: int(x.replace(',', '')) if type(x) == str else x)
df['Votes'] = df['Votes'].fillna(df['Votes'].dropna().mean())

# Trích xuất danh sách các thể loại từ cột genre
df['genre'] = df['genre'].apply(lambda x: x.split(', '))
print(df)

# Chia cột genre thành nhiều dòng
explode_genre_df = df.explode('genre')
print(explode_genre_df)

# Groupby df theo genre
grouped_genre_df = explode_genre_df.groupby('genre')

# A. Thời lượng trung bình, số votes trung bình của các bộ phim theo từng thể loại
print('Thời lượng trung bình, số votes trung bình của các bộ phim theo từng thể loại:')
print(grouped_genre_df[['Minutes', 'Votes']].mean())

# B. Ratings trung bình của các thể loại là bao nhiêu?
print('Ratings trung bình của các thể loại:')
print(grouped_genre_df['Rating'].mean())
