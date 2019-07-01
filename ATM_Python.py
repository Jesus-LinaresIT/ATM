#!/usr/bin
import math

print("\nStarting ATM...")

print("\n-------------Operations ATM---------------")

print("\n-Insert cash into the account --------------------> I")
print("-Withdraw cash from the account ------------------> W")
print("-Show money available ----------------------------> S")
print("-Exit --------------------------------------------> E")

credit = 1200

operation = input("\nType key of the Operation: ").upper()

if operation == "I":
	numOne = float(input("Type the amount of money to enter: "))
	credit += numOne

	print(f"\n-----THE OPERATION SUCCESS-----")
	print(f"\n\tThe credit your account current is: ${credit} dolars")	

elif operation == "W":
	numOne = float(input("Type the amount of money to withdraw: "))
	if numOne > credit:
		print("\n\t'The amount of money you want to withdraw \n\tis greater than your current account.'")
	elif numOne > 300 or numOne < 5:
		print("\n\t'The amount entered is greater or less than that allowed'")
	else:
		credit -= numOne

		print(f"\nTHE OPERATION SUCCESS")
		print("-----Withdraw your money------.")
		print("\nDo you want to know the amount your account current?")
		print("\n-Yes -------------------------------------------> Y")
		print("-No --------------------------------------------> N")

		operation = input("\nType key of the Operation: ").upper()

		if operation != "Y" and operation != "N":
			print("\n\tERROR the Key.")
		else:
			if operation == "Y":
				print(f"\n\tThe credit your account current is: ${credit} dolars")
			else:
				print("\n\tFinishid Operation...")

elif operation == "S":
	print(f"\n\tThe credit your account current is: ${credit} dolars")

elif operation == "E":
	print("\n\tFinishid Operation...")

else:
	print("\n\tERROR entered the key.")



print("\nThanks for prefering us...")
print("\nFinishid ATM...")