# 問2-1
# 配列の値nをすべて調べ、偶数であれば「nは偶数です。」
# 奇数であれば、「nは奇数です。」と出力するプログラムを記述せよ
# ルール：
#   forを用いる
# a = [10, -5, 0, 29, 6, 2, 77, 8]

# for i in a:
#   if i % 2 == 0:
#     print(i, "は偶数です")
#   else:
#     print(i, "は奇数です")

# 問2-2
# nは1以上5以下の整数とする。3のn乗と2のn乗の差を求めて出力するプログラムを出力せよ
# ルール：
#   forを用いる
#   3のn乗と2のn乗は配列を定義してはいけない
x = 3
y = 2

for i in range(1, 6):
  result_x = x ** i
  result_y = y ** i
  print(i, "乗の差分 = ", result_x - result_y)

# 問2-3
# ①✕
# ②✕
# ③◯
# ④✕
# ⑤✕
# ⑥◯