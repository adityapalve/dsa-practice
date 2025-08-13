n = int(input())
def melon(n):
  if n<4: 
    return print("NO")

  if n%4 == 0 or n%4 == 2:
    print("YES")
  else:
    print("NO")

melon(n)
