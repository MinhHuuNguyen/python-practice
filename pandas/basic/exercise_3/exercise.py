# Bài tập 2: Hãy tiến hành xử lý, làm sạch bộ dữ liệu Raw_credits và tìm ra các thông tin sau:
# Điểm số trung bình imdb_score của tất cả các bộ phim là bao nhiêu? Của từng thể loại là bao nhiêu?
# Số lượng imdb votes của tất cả các bộ phim và của riêng từng thể loại
# Tìm ra số lượng trung bình imdb_votes và imdb_score theo từng năm release
# Hãy suy luận xem liệu có mối liên hệ nào giữa imdb_votes, imdb_score với năm release không?

import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('data/raw_titles.csv')

# Hiển thị thông tin của dữ liệu
print(df)

# Hiển thị các cột của dữ liệu
print(df.columns)

# Xử lý dữ liệu cột imdb_score và imdb_votes
print('So luong gia tri khuyet thieu tren cot imdb_score', df['imdb_score'].isna().sum())
print('So luong gia tri khuyet thieu tren cot imdb_votes', df['imdb_votes'].isna().sum())

# # Cách 1: Loại bỏ các dòng có giá trị khuyết thiếu trên cột imdb_score và imdb_votes
# df = df.dropna(subset=['imdb_score'])
# df = df.dropna(subset=['imdb_votes'])

# Cách 2: Thay thế giá trị khuyết thiếu
# trên cột imdb_score bằng giá trị trung bình của cột imdb_score và imdb_votes
df['imdb_score'] = df['imdb_score'].fillna(df['imdb_score'].dropna().mean())
df['imdb_votes'] = df['imdb_votes'].fillna(df['imdb_votes'].dropna().mean())

# Format dữ liệu cột genres thành list
df['genres'] = df['genres'].apply(eval)

print(df)

# Điểm số trung bình imdb_score của tất cả các bộ phim là bao nhiêu? Của từng thể loại là bao nhiêu?
print('Điểm số trung bình imdb_score của tất cả các bộ phim:', df['imdb_score'].mean())
print('Điểm số trung bình imdb_score của từng thể loại:')
explode_genre_df = df.explode('genres')
grouped_genre_df = explode_genre_df.groupby('genres')
print(grouped_genre_df['imdb_score'].mean())

# Số lượng imdb votes của tất cả các bộ phim và của riêng từng thể loại
print('Số lượng imdb votes của tất cả các bộ phim:', df['imdb_votes'].mean())
print('Số lượng imdb votes của từng thể loại:')
print(grouped_genre_df['imdb_votes'].mean())

# Tìm ra số lượng trung bình imdb_votes và imdb_score theo từng năm release
grouped_year_df = df.groupby('release_year')
print('Số lượng trung bình imdb_votes theo từng năm release:')
print(grouped_year_df['imdb_votes'].mean())
print('Số lượng trung bình imdb_score theo từng năm release:')
print(grouped_year_df['imdb_score'].mean())

# Hãy suy luận xem liệu có mối liên hệ nào giữa imdb_votes, imdb_score với năm release không?
mean_votes_grouped_year_df = grouped_year_df['imdb_votes'].mean()
plt.figure(figsize=(20, 6))
plt.scatter(mean_votes_grouped_year_df.index, mean_votes_grouped_year_df)
plt.xlabel('release_year')
plt.ylabel('imdb_votes')
plt.savefig('imdb_votes.png')

mean_score_grouped_year_df = grouped_year_df['imdb_score'].mean()
plt.figure(figsize=(20, 6))
plt.scatter(mean_score_grouped_year_df.index, mean_score_grouped_year_df)
plt.xlabel('release_year')
plt.ylabel('imdb_score')
plt.savefig('imdb_score.png')
