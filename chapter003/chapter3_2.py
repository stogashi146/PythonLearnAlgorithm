# キューの仕組み
# 最初に入れたデータを最初に取り出す仕組み。待ち行列みたいなイメージ
# キューにデータを入れることを、enqueue
# 取り出すことを、dequeue

MAX = 6
que = [0]*MAX
head = 0
tail = 0

def enqueue(d):
  global tail
  # -1だと終端という意味
  nt = (tail + 1) % MAX
  
  if nt == head:
    print("これ以上データは入れられません")
  else:
    que[tail] = d
    tail = nt
    print("データ", d, "を追加しました")

def dequeue():
  global head
  if head == tail:
    print("取り出すデータが存在しません")
    return None
  else:
    d = que[head]
    # headを次の位置にする
    head = (head + 1) % MAX
    return d

for i in range(6):
  enqueue(i)
  
for i in range(6):
  d = dequeue()
  
  print("取り出したデータ", d)