# 2から100までの整数が素数か調べる。素数であればその数を出力する
# 前提：n / 2からの数で割り切れれば素数である
# ルール：
#   二重ループを用いる
for i in range(2, 101):
  h = i // 2
  is_prime = True
  for j in range(2, h+1):
    if i % j == 0:
      is_prime = False
      break
  
  if is_prime:
    print(i)