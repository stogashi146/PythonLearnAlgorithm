# スタックの仕組み
# 追加：データを積み重ねて保持する
# 取り出す：最後に入れたデータから取り出す

MAX = 5
stack = [0]*MAX
sp = 0

def push(d):
  global sp
  if sp < MAX:
    stack[sp] = d
    sp  = sp + 1
    print("データ", d, "を追加しました")
  else:
    print("これ以上データを入れられません")
    
def pop():
  global sp
  if sp > 0:
    sp = sp -1
    return stack[sp]
  else:
    print("取り出すデータが存在しません")
    return None

for i in range(6):
  push(i)
for i in range(6):
  d = pop()
  print("取り出したデータ", d)
