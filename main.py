import time, os

while(True):
  print("Press 1 for TopTaxi")
  print("Press 2 for Phones4us")
  print("Press 3 for aricalc")
  menuSelect = input("> ")

  if(menuSelect=="1"):
    os.system('clear')
    import toptaxi
  elif(menuSelect=="2"):
    os.system('clear')
    import phones4us
  elif(menuSelect=="3"):
    os.system('clear')
    import aricalc
  else:
    print("ERROR")

  time.sleep(1)
  os.system('clear')
  


#price = 0.0
#size = input("Size: ").lower()
#colour = input("Colour: ").lower(()
#if(colour=="blue"):
  #if(size=="s"):
    #price = 9.99
#elif(size=="m"):
  #price = 10.99
#elif(size=="l"):
  #price = 11.99
#elif(colour=="red"):
	#if(size=="s"):
		#price = 10.99
	#elif(size=="m"):
		#price = 12.49
	#elif(size=="l"):
		#price = 13.99
#elif(colour=="black"):
	#if(size=="s"):
		#price = 12.99
	#elif(size=="m"):
		#price = 14.99
	#elif(size=="l"):
		#price = 16.99