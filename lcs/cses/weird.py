n = int(input())
def foo(n):
  r = []
  def foo2(n,r):
    r.append(str(n))
    if n==1:
      return n

    if n%2==0:
      n = n//2
    else:
      n = n*3+1
    foo2(n,r)
  
  foo2(n,r)
  ans = " ".join(r)
  print(ans)

foo(n)