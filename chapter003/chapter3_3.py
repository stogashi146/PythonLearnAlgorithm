# リストの仕組み
# 線型リスト
# 種類：片方向リスト、双方向リスト、循環リストが存在する
# リストの要素1つ1つをノードと言い、それぞれ繋がっている
# メリット：
#   リストの追加・削除はメモリのデータの位置をずらさないで可能

MAX = 5
data = [None]*MAX
pointer = [None]*MAX
head = 0

def add_list(d):
  n = -1
  for i in range(MAX):
    if data[i] == None:
      n = i
      break
  if n == -1:
    print("データ領域の空きがありません")
    return False
  for i in range(MAX):
    if data[i] != None and pointer[i] == None:
      pointer[i] = n
      break

  data[n] = d
  pointer[n] = None
  print("データ", d, "を追加しました")
  return True

def del_list(d):
  global head
  n = -1
  for i in range(MAX):
    if data[i] == d:
      n = i
      break
  if n == -1:
    print("そのデータは存在しません")
    return False
  if n != head:
    for i in range(MAX):
      if pointer[i] == n:
        pointer[i] = pointer[n]
  else:
    head = pointer[n]
    if head == None:
      head = 0
  
  data[n] = None
  pointer[n] = None
  print("データ", d, "を削除しました")
  return True

def put_list():
  p = head
  while True:
    print(data[p], end="➾")
    if pointer[p] == None:
      print("EOF")
      break
    p = pointer[p]
    
for i in range(10, 70, 10):
  add_list(i)
  
del_list(10)
put_list()