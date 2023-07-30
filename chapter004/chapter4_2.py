# 二分捜索
# 調べるデータが順に並んでいる場合、使用できる。線型より早い
# 


data = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 80, 93, 100]
key = int(input("探す値を入力してください"))
left = 0
right = len(data) - 1
flg = False

while left <= right:
  mid = (left + right) // 2
  print("L={} M={} R={}".format(left, mid, right))
  # 見つかったら
  if data[mid] == key:
    print("data[{}]が{}です".format(mid, key))
    flg = True
    break
  # data[mid]とりkeyが大きいとき
  if data[mid] < key:
    left = mid + 1
  else:
    right = mid -1
    
if flg == False:
  print("その値は見つかりませんでした。")