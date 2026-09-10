#  prime number

num=int(input('Enter a number'))

if num==1:
    print(num,'is not a prime number')
    for i in range(2,(num+1)):
       if num%i==0:
           print(num,"is not a prime number")

       else:
           print(num,'prime number')


              