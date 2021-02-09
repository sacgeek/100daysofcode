# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height * height)

if bmi < 18.5:
  print (f"Your BMI is {round(bmi, 1)} and you are underweight.")
elif bmi < 25:
  print (f"Your BMI is {round(bmi, 1)} and you have a normal weight.")
elif bmi < 30:
  print (f"Your BMI is {round(bmi, 1)} and you are slightly overweight.")
elif bmi < 35:
  print (f"Your BMI is {round(bmi, 1)} and you are obese.")
else:
  print (f"Your BMI is {round(bmi, 1)} and you are clinically obese.")