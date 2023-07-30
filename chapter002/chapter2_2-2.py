# 1からnまで足し合わせた関数を定義する
# ルール：
#   いくつまで足し合わせるか(nの値)を関数の引数で受け取る
#   関数は足し合わせた値をreturnで返す

def addup(n):
  total = 0
  for i in range(1, n+1):
    total += i

  return total

print(addup(2))