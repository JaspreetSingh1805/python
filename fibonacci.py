def fib(n):
  a = 1
  b = 1 
  print(a)
  
  if(n==1):
      return
  print(b)
  for i in range(2,n):
      
      c = a+b
      a = b
      b = c
      print(c)
fib(10)

