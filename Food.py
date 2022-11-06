
import random
print("Welcome to The Aspen Online Ordering Platform")


username=input("Please enter name: ")
address= input("Please enter address: ")
phone=input("Enter phone number: ")



print("Menu Options: \n1) Kofta Sandwich 30LE \n2) Fried Chicken Sandwich 30 LE \n3) Nutella Sandwich \
40 LE \n4) Half Chicken 90 LE \n5) Chicken 160 LE\n6) Order Complete")

orderno=random.randint(1,1000)

item1=0
item2=0
item3=0
item4=0
  
item5=0
from datetime import datetime
timing=datetime.now()


  
meal=int(input("Enter meal number: "))

amount=int(input("How much?: "))
while(meal!=6):
    
    if meal==1:
        item1+=amount
    if meal==2:
         item2+=amount
    if meal==3:
        item3+=amount
    if meal==4:
        item4+=amount
    if meal==5:
        item5+=amount
 
    meal=int(input("Enter meal number: "))
    if meal==6:
        break
    amount=int(input("How much?: "))

total=item1*30+item2*30+item3*40+item4*90+item5*160
print("Your total is "+str(total)+ " EGP")

name=str(timing)+".txt"
name=name.replace(' ',',')
name=name.replace(':','-')
order="Order #"+str(orderno)+" Time: "+name.replace('.txt','')+"\n"+"Customer Name: "+username+"\nDelivery Address: "+address+"\nPhone Contact: "+phone+"\n"
if item1>0:
    order+="Kofta Sandwich X" +str(item1)+"\n"
if item2>0:
    order+="Chicken Sandwich X" +str(item2)+"\n"
if item3>0:
    order+="Nutella Sandwich X" +str(item3)+"\n"
if item4>0:
    order+="Half Chicken X" +str(item4)+"\n"
if item5>0:
    order+="Full chicken X" +str(item5)+"\n"
order+="Total: "+str(total)+" EGP"



f = open(name,"w")
f.write(order)
f.close()



    

    
    

