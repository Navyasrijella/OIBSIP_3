def calci_bmi(weight,height):
    return round((weight / height**2),2)

print("Welcome to the BMI calculator.")

w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))


bmi = calci_bmi(w, h)

print("Your BMI is: ", bmi)


if bmi <= 18.5:
    print("Oops!You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Awesome!It's healthy weight.")
elif 25 < bmi <= 29.29:
    print("Eee!You are overweight.")
else:
    print("Oh no!You are obese.")