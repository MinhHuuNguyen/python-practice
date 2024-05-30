# Bài tập 4: Hãy sử dụng Python để giải bài toán cổ sau : “Vừa gà vừa chó, Bó lại cho tròn, Ba mươi sáu con, Một trăm chân chẵn“

# Đặt số con gà là x, số con chó là y
# Theo đề bài ta có hệ phương trình:
# x + y = 36
# 2x + 4y = 100
# Giải hệ phương trình trên ta được:
# x = 22, y = 14
# Vậy có 22 con gà và 14 con chó

from sympy import symbols, Eq, solve

x, y = symbols('x y')

eq_1 = Eq(x + y, 36)
eq_2 = Eq(2 * x + 4 * y, 100)

result = solve((eq_1, eq_2), (x, y))

print(f"Vậy có {result[x]} con gà và {result[y]} con chó")
