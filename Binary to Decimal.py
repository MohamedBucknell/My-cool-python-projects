print("Decimal to Binary Converter")

n=input("Enter binary number: ")
n=int(n)
s=""
        
while n>0:
    if n%2==0:
        s="0"+s
        
    else:
        s="1"+s
    n=n//2

print(s)

        

    

