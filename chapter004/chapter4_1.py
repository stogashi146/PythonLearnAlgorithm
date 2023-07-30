# 線型捜索
# 総当りで調べる方法
# メリット：
#   基本となる捜索方法なので、扱いやすい
# デメリット：
#   データ量が多く目的の値が後方にある場合、パフォーマンスが悪い

data = [57, 48, 46, 52, 45, 59, 61, 60, 49, 71]
n = len(data)
# 探したい数字
key = 60

# 実装例1
flg = False
for i in range(n):
  if data[i] == key:
    print("data[{}]が{}です".format(i, key))
    flg = True
    break

if flg == False:
  print(str(key)+"は存在いません")
  
# 実装例2
while i < n and data[i] != key:
  i += 1

if i == n:
  print(str(key) + "は存在しません")
else:
  print("data[{}]が{}です".format(i, key))

# 実装例3

data = [
  ["佐藤", "000-0000-0000"],
  ["鈴木", "111-1111-1111"],
  ["高橋", "222-2222-2222"],
  ["田中", "333-3333-3333"],
]

n = len(data)
s = input("検索する相手の名字は？")

i = 0
while i < n and data[i][0] != s:
  i += 1

if i == n:
  print("その名は登録されていません")
else:
  print(data[i][0] + "さんの番号は" + data[i][1] + "です")