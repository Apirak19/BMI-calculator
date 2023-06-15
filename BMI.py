print("This is BMI calculator")
weight = int(input("your weight (kg):"))
height = int(input("your height (cm):"))
BMI = weight/((height/100)**2)

if BMI<30:
    if BMI<19:
        BMIR = "UnderWeight"
    elif 19<BMI<25:
        BMIR = "NormalWight"
    elif 25<BMI<30:
        BMIR = "OverWeight"
else:
    BMIR = "... Go see a doctor ASAP!!"

print("Your BMI: ", BMI)
print("You are ", BMIR)
print("Thank you for using this program")
