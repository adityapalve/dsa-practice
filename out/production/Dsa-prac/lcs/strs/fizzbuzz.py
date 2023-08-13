def fizz():
  i=0
  while(i<=20):
    if(i % 15 == 0 and i!=0):
      print("FizzBuzz")
    else:
      if(i%3==0 and i!=0):
        print("Fizz")

      elif(i%5==0 and i!=0):
        print("Buzz")
      
      else:
        print(i)
    i+=1
  return 0

fizz()