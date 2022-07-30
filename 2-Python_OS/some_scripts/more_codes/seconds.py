#!/usr/bin/env python3

def time_converter(hours=0,minutes=0,seconds):
	return 3600*hours + 60*minutes + seconds

print("Welcome to time converter")
cont = 'y'
while(cont.lower() == 'y'):
	hours = int(input("Enter the Hours "))
	minutes = int(input("Enter the Minutes "))
	sec = int(input("Enter the Seconds "))
	print()
	print("Tht's {} seconds".format(time_converter(hours,minutes,sec)))
	print()
	cont = input("Do you want to continue? [y to continue]")

print("Good Bye!")
#Write
