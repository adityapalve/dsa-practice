n = int(input())
words = [input() for i in range(n)]

def foo(words):
  for word in words:
    if len(word)<=10:
      print(word)
    else:
      print(f'{word[0]}{len(word[1:-1])}{word[-1]}')\

foo(words)