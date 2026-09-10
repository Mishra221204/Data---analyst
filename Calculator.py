# write a program to  build calculator  operation


print("1.Addition")
print("2.Multiply")
print("3.division")
print("4.Substraction")

user=int(input("Enter Choice Mathmetical Calculation:"))

a=int(input("Enter a First Number :"))
b=int(input("Enter a Secand Number :"))

def calculator(a,b):
    if user == 1:
        print("Addition num a + b :",a+b)
    elif user==2:
        print("Multiply num a*b :",a*b)
    elif user == 3:
        print("Division num a/b:",a/b)
    elif user == 4:
        print ("Substraction num a-b",a-b)
    else :
        print("Invalide Choices")


calculator(a,b)
        
