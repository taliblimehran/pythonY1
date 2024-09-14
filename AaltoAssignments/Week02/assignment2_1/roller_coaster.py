#Roller coaster height checker
def main():
#Ask the user for their height
   height = int(input("How tall are you (cm)\n"))

   #Check if the user is tall enough for the ride
   if height >= 140:
    print("You are good to go. Have fun!")
   else:
    print("Unfortunately you are too short for this ride.")

main()
