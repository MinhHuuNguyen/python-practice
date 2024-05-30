# Bạn hãy dùng Pandas đọc file dữ liệu All_player_stats và tìm các thông tin sau:
# Câu 1: Thông tin tổng quan về bộ dữ liệu này
# Câu 2: Sắp xếp dataframe theo thứ tự tăng dần/giảm dần số bàn thắng
# Câu 3: Hãy tìm ra cầu thủ nào bị nhiều thẻ vàng nhất, nhiều thẻ đỏ nhất, thi đấu nhiều nhất
# Câu 4: Hãy tìm ra cầu thủ thi đấu nhiều nhất của từng CLB
# Câu 5: Hãy tìm ra cầu thủ ghi nhiều bàn thắng nhất, với vị trí Defender

import pandas as pd
import numpy as np

# Đọc dữ liệu từ file csv
df = pd.read_csv('all_players_stats.csv')
print(df)

print(df.info())

print(df.describe())

sorted_df = df.sort_values(by='RedCards', ascending=False)
print(sorted_df)
# Apearances: Antonio Rüdiger - 54
# YellowCards: Conor Gallagher, James Tarkowski, Antonio Rüdiger - 12
# RedCards: Granit Xhaka, Aaron Cresswell, Raúl Jiménez, Ezri Konsa - 2

print(df[df.Apearances == np.max(df.Apearances)])
print(df[df.YellowCards == np.max(df.YellowCards)])
print(df[df.RedCards == np.max(df.RedCards)])

grouped_df = df.groupby('Team')
print(grouped_df)

for team, group_df in grouped_df:
    print('\n\n', team)
    # print(group_df[group_df.Apearances == np.max(group_df.Apearances)])
    print(group_df.sort_values(by='Apearances', ascending=False).head(1))
    print(group_df.sort_values(by='Apearances', ascending=False).reset_index().loc[0])


def check_defender(position):
    return 'Defender' in position

# Bước 1: Lọc ra vị trí Defender
df['check_defender'] = df['Position'].apply(check_defender)
print(df.loc[df.check_defender == True])

# Bước 2: Lấy ra cầu thủ ghi nhiều bàn thắng nhất
print(df.loc[df.check_defender == True].sort_values(by='Goals', ascending=False).head(1))
