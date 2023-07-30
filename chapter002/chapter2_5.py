# nの階乗(n!)を求める
# 10!を求める
# ルール：
#   forを用いる
# a = 10

# for i in range(9, 1, -1):
#   a = a * i

# print("10! = ", a)

# ルール：
#   再帰関数を求める
def fact(n):
  if n == 0:
    return 1
  
  return n * fact(n - 1)

for i in range(0, 21):
  print(i, "! = ", fact(i))

