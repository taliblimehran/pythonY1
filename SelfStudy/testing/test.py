import sys
from math import floor

#print(sys.version)
#print("hello world")
#def main():
    #fahrenheit = 78.5
    #celcius = (fahrenheit -32) *5.0 / 9.0
    #print(celcius)

    #name = input("Enter your name: ")
    #print("your name is ", name)
    #print("Welcome to the basic course in programming!")

    # fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    # celsius = (fahrenheit - 32) * 5.0 / 9.0
    # print(fahrenheit, "F is", celsius, "C")

#     width = float(input("Enter the width of the room in metres: \n"))
#     length = float(input("Enter the length of the room in metres: \n"))
#     area = floor(width * length)
#     print("The area of the room is", area, "square metres")
#
# main()

# def main():
#     print("This program calculates the price of a phone call.")
#     fixedcost = float(input("Enter the fixed cost:\n"))
#     minuteprice = float(input("Enter the minute price:\n"))
#     duration = float(input("Enter the duration of the call in minutes:\n"))
#     price = fixedcost + duration * minuteprice
#     print("The price of the phone call is", price, "euros.")
#
# main()

# def main():
#     print("This program expresses a given time period (hours, minutes, seconds) in seconds.")
#     hours = int(input("Enter how many hours the time period spans:\n"))
#     minutes = int(input("Enter how many minutes the time period spans:\n"))
#     seconds = int(input("Enter how many seconds the time period spans:\n"))
#     time_in_seconds = hours * 3600 + minutes * 60 + seconds
#     print("The length of the time period in seconds is", time_in_seconds)
#
# main()

def main():
    duration_seconds = int(input("Enter a time period in seconds:\n"))
    hours = duration_seconds // 3600
    remainder = duration_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    print("The converted duration is", hours, "h", minutes, "min", seconds, "s.")

main()

