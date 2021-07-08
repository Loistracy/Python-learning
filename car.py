print("type help to ask for instruction")

instraction = input()
instraction = help

if instraction == help:
      print(''' 
      start - to start the car
      stop - to stop the car
      quit- to exit  ''' )
else:
      print("please type help")

instra = input()
instra = "start"
    
if instra == "start":
    print("car started.")

elif instra == "stop":
    print("car stopped")

elif instra == "quit":
    exit()
