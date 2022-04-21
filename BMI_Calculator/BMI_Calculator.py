def Details():
    height = float(input("Enter the height (in cm) : "))/100
    weight = float(input("Enter the weight (in kg) : "))
    BMI = weight/(height*height)
    return BMI

BMI = Details()

def Calc(BMI):
    if BMI > 0:
        if BMI < 18.5:
            print("Underweight")
        elif BMI >= 18.5 and BMI < 25:
            print("Normal")
        elif BMI >= 25 and BMI < 30:
            print("Overweight")
        elif BMI >= 30 and BMI < 35:
            print("Obese")
        else:
            print("Extremely Obese")
    else:
        print("Enter valid details")
        BMI = Details()
        Calc(BMI)

    return BMI

BMI = Calc(BMI)
print(f"BMI value : {BMI}")
