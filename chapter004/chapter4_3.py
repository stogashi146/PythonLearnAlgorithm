# 木捜索
# 二分木捜索
# 調べるデータが順に並んでいる場合、使用できる。線型より早い
# 通りがけ順：左の子を調べ、根を調べ、右の子を調べる

# 実装例（通りがけ順）
LEFT = 0
RIGHT = 1
DATA = 2
node = [
  [1, 2, 10],
  [3, 4, 5],
  [5, None, 12],
  [None, None, 2],
  [6, 7, 8],
  [None, None, 11],
  [None, None, 6],
  [None, None, 9],
]

def traverse(p):
  if p != None:
    # 引数を左の子として関数を実行
    traverse(node[p][LEFT])
    # データ値を出力
    print(node[p][DATA])
    # 引数を右の子として関数を実行
    traverse(node[p][RIGHT])

print("二分捜索木を通りがけ順に巡回")
traverse(0)

