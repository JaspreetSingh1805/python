num = int(input("Enter a value here:  "))
is_prime = True
if(num<=1):
    print("Number neither prime or composite")
else:
     for i in range(2,num):
        if(num%i==0):
          print("not prime")
          is_prime = False
          break
     if(is_prime):
        print("Prime no")