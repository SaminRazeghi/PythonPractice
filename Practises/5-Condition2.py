from tkinter import W


print("Please enter your height:")
Height = int(input())
print("Please enter your weight:")
Weight = int(input())
if Height < 150:
    if Weight < 40:
        print("Underweight")
    elif Weight > 50:
        print("Overweight")
    else:
        print("Normal")
elif Height > 180:
    if Weight < 80:
        print("Underweight")
    elif Weight > 90:
        print("Overweight")
    else:
        print("Normal")
else:
    if Weight < 50:
        print("Underweight")
    elif Weight > 80:
        print("Overweight")
    else:
        print("Normal")
