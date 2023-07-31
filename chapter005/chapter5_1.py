# 選択ソート
# 処理の流れ：
# 1. データの中で最も小さな値を探し、先頭と入れ替える
# 2. 先頭以外から、最も小さな値を探して先頭と入れ替える
# データがなくなるまで繰り返す

# 実装例
data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]
print(data, "元のデータ")

for i in range(0, 9):
  # 最小値の値を保持する編集
  min = i
  for j in range(i+1, 10): # 小さい値を探す
    if data[j] < data[min]:
      min = j
  data[i], data[min] = data[min], data[i]
  
print(data, "ソート後のデータ")