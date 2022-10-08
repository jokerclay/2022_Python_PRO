print("Welcome to the rollercoaster !");
height = int(input("what is your height in cm? \n"));

if height > 120:
    print("you can ride the rollercoaster! ");
    age = int(input("what is your age? \n"));

    if (age <  12):
        print("Please pay $5");
    elif (age <=  18):
        print("Please pay $7");
    else:
        print("Please pay $12");
else:
    print("Sorry, you have to grew taller before you can ride !");

