#BMI = (weight in pounds * 703) / (height in inches * height in inches)

weight = int(input("Please enter your weight in pounds: "))
height = int(input("Please enter your height in inches: "))

BMI = (weight * 703) / (height * height)
print("Your BMI is: " + BMI)

if BMI < 18.5:
	print("You are underweight")
	print("Your health risk is minimal")
elif BMI <= 24.9:
	print("You are normal weight")
	print("Your health risk is minimal")
elif BMI <= 29.9:
	print("You are overweight")
	print("Your health risk has increased")
elif BMI <= 34.9:
	print("You are obese")
	print("Your health risk is high")
elif BMI <= 39.9:
	print("You are severely obese")
	print("Your health risk is very high")
else:
	print("You are morbidly obese")
	print("Your health risk is extremely high")
