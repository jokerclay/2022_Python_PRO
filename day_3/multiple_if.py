#
# all the condition will to be checked
# 

print("Welcome to the rollercoaster !");
height = int(input("what is your height in cm? \n"));
bill = 0;

if height > 120:
    print("you can ride the rollercoaster! ");
    age = int(input("what is your age? \n"));

    if (age <  12):
        bill = 5;
        print("Please pay $5");
    elif (age <=  18):
        bill = 7;
        print("Please pay $7");
    else:
        bill = 12;
        print("Please pay $12");
    want_pic = input("Do you want to take a picture ? Y/N : \n")
    
    if(want_pic == "Y"):
        bill += 3;
        print(f"your bill is ${bill}");

else:
    print("Sorry, you have to grew taller before you can ride !");

