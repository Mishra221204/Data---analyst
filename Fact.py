n=int(input("Enter the value of factorial number that i find:"))
fact=1
for i in range(1,n+1):
    fact=fact*i;
    print(f"factorial is {fact}")