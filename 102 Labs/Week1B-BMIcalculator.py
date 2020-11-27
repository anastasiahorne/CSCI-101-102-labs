#Anastasia Horne
#102 Section-G
#Week 1- Part B
#References: No one
#Time: 20 minutes
Weight= int(input("In pounds, Weight>"))
Height= int(input("In inches, Height>"))
Weight_kilograms= Weight * 0.454
Height_meters= Height * 0.0254
#BMI means Body-Mass Index
BMI= Weight_kilograms / (Height_meters ** 2)
print("Your BMI is:")
print("OUTPUT",round(BMI,1))
