# 木
# ツリー構造になっているノードのこと
# 二分岐
# 1つのノードから、2つのノードに分岐する構造
# 以下の例では、配列を用いて二分岐を定義
node = [
  # [左の枝がどのノードに繋がるか, 右の枝がどのノードに繋がるか, データ]
  [1, 2, 10],
  [3, 4, 20],
  [5, None, 30],
  [None, None, 40]
]

LEFT = 0
RIGHT = 1
DATA = 2
node = [
  [1, 2, 10],
  [3, 4, 20],
  [5, None, 30],
  [None, None, 40],
  [6, 7, 50],
  [None, None, 60],
  [None, None, 70],
  [None, None, 80],
]

MAX = len(node)

print("指定の番号のノートを調べます")
print("何も入力せずにEnterを押すと終了します")

while True:
  s = input("number=")
  if s == "":
    break
  
  n = int(s)
  if 0 <= n and n < MAX:
    print("node{}の値は{}".format(n, node[n][DATA]))
    le = node[n][LEFT]
    if le != None:
      print("左の子は" + str(node[le][DATA]))
    else:
      print("左の子は存在しません")
    
    ri = node[n][RIGHT]
    if ri != None:
      print("右の子は" + str(node[ri][DATA]))
    else:
      print("右の子は存在しません")
  else:
    print("0から" + str(MAX-1) + "の範囲で入力してください")