# 点数の平均値を求める
# ルール：
#   点数は配列で定義する
#   forを使用する
points = [70, 98, 92, 88, 64]

total_point = 0
for i in points:
  total_point += i

point_length = len(points)

print(total_point / point_length)