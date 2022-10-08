height = input("enter your height in m : ");
weight = input("enter your weight in kg : ");

# BMI = weight / height ^2
# More about BMI : https://en.wikipedia.org/wiki/Body_mass_index
# print BMI as a int

bmi = round(float(weight) / (float(height)**2));
bmi_status = "";

if (bmi < 18.5):
    bmi_status = "underweight";
elif(bmi < 25):
    bmi_status = "normal weight";
elif(bmi < 30):
    bmi_status = "overweight";
elif(bmi < 35):
    bmi_status = "obese";
else:
    bmi_status = "cinically obese";

print(f"your BMI is : {bmi}, and you are {bmi_status}");


