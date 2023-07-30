import random
n = 0
r = random.randint(1, 100)

print("1から100までの数を当てるゲームです")
while True:
  n += 1
  a = int(input("数を入力してください"))

  if r == a:
    print(str(n) + "回で正解です")
    break
  if r > a:
    print("それよりも大きい数です")
  else:
    print("それよりも小さい数です。")
