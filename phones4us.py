import time, os
print("Welcome To Phones4Us")
totalCost = 0
customername=input("Enter your name")
phonename=input("Enter name of phone")
phonesize=input("Enter size of phone")
contract=int(input("Enter contract length in months"))
phonecost = 0
#monthlycost = 10 + model * contract
size = input("Size:[Mini, Regular, Max] ").lower()
model = input("Model: ").lower()
if(model=="iphone12"):
  if(size=="mini"):
    price =799.99
  elif(size=="regular"):
    price = 999.99
  elif(size=="max"):
    price = 1190.00
elif(colour=="iphone12 Pro"):
  if(size=="mini"):
    price = 10.99
  elif(size=="regular"):
    price = 1099.00
  elif(size=="max"):
    price = 1190.00  
print("price", phonecost)
monthlycost = 10 + (phonecost / contract)
print("monthlycost", round(monthlycost,2))
