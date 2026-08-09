# Write a Python Program to calculate your Body Mass Index.


def calculate_body_mass_index(height:float | int, weight:float | int):
    return round(weight / height ** 2, 2)


bmi = calculate_body_mass_index(1.6764, 67) #height in meters

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("I have no idea about you, please consult to a doctor.")
