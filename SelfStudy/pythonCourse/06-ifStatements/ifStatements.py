if = Do some code only IF some condition is true
     Else do something else

age = int(input("Enter your age: \n"))

if age > 100:
    print("You are too old to sign up \n")
elif age < 0:
    print("you haven't been born yet \n")
elif age >= 18:
    print("You are now signed up \n")
else:
    print("You must be 18+ to sign up \n")

response = input("would you like food? (Y/N): ")

if response == "Y":
    print("Have some food")
else:
    print("No food for you!")

name = input("Enter your name\n")

if name == "":
    print("You did not type your name")
else:
    print(f"Hello {name}")

online = True

if online:
    print("The User is online ")
else:
    print("The User is offline ")