print("TOP TAXI LTD")
totalCost = 0
#totalCost = price * distance
#What variables do you need to define before the loop begins?
while(True):
  #your code replaces this pass command
  pkuplocation= input("Where is your pickup location")
  finaldestination = input("Where is your final destination ")
  distance = float(input("How many miles is your destination"))
  thisCost = distance*0.5
  if(distance>15):
    thisCost *= 0.7
    print("Long distance journey")
  print("Subtotal: ", round(thisCost,2))
  totalCost += thisCost
  print("Total:", round(totalCost,2))
  exit= input("Exit? y/n").lower()[0]
  if (exit == "y"):
    break