# Bạn hãy sử dụng file dữ liệu sau link và thực hiện dùng pandas để tìm ra các thông tin sau:
# Bài tập 1: Có tất cả bao nhiêu đơn hàng? Có tất cả bao nhiêu khách hàng đã mua hàng?
# Bài tập 2: Category nào được mua nhiều nhất?
# Bài tập 3: Subcategory nào được mua nhiều nhất?
# Bài tập 4: Tổng doanh số của tất cả các đơn hàng là bao nhiêu?
# Bài tập 5: Tổng lợi nhuận của tất cả các đơn hàng là bao nhiêu?
# Bài tập 6: Tổng doanh số và lợi nhuận của từng Category là bao nhiêu?

import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('data/Data_Practices_Sales.csv')

# Hiển thị thông tin của dữ liệu
print(df)

# Hiển thị các cột của dữ liệu
print(df.columns)

# Bài tập 1: Có tất cả bao nhiêu đơn hàng? Có tất cả bao nhiêu khách hàng đã mua hàng?
print('===>>> So don hang:', len(df['Order ID'].unique()))
print('===>>> So khach hang da mua hang:', len(df['Customer ID'].unique()))

# Bài tập 2: Category nào được mua nhiều nhất?
print(df['Category'].value_counts())
print('===>>> Category duoc mua nhieu nhat:', df['Category'].value_counts().index[0])

# Bài tập 3: Subcategory nào được mua nhiều nhất?
print(df['Sub-Category'].value_counts())
print('===>>> Subcategory duoc mua nhieu nhat:', df['Sub-Category'].value_counts().index[0])

# Bài tập 4: Tổng doanh số của tất cả các đơn hàng là bao nhiêu?
print('===>>> Tong doanh so cua tat ca cac don hang:', df['Quantity'].sum())

# Bài tập 5: Tổng lợi nhuận của tất cả các đơn hàng là bao nhiêu?
print('===>>> Tong loi nhuan cua tat ca cac don hang:', df['Profit'].sum())

# Bài tập 6: Tổng doanh số và lợi nhuận của từng Category là bao nhiêu?
print(df.groupby('Category').sum()[['Quantity']])
print(df.groupby('Category').sum()[['Profit']])
