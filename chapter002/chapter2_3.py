# 九九の段をすべて出力する
# ルール：
#   二重ループを用いる
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i, "x", j, "=", i * j)

# 別解
# 段毎にインラインで表示する
# formatは,文字列の中括弧に引数を展開する
for i in range(1, 10):
  k = ""
  for j in range(1, 10):
    k = k + "{} * {} = {:2d}  ".format(i , j, i*j)
  
  print(k)