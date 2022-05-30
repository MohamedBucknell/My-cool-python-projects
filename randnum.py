import random
print("Guess number between 1 and 100")
guess=0
cont=""
s=1
i=100
while True:
    guess=random.randint(s,i)
    print("Is it "+str(guess))
    cont=input("Bigger or less or correct b/l/y")
    if cont=="y":
        break
    if cont=="b":
        s=guess
        
    if cont=="l":
        
        i=guess
        
        
        
    
    
