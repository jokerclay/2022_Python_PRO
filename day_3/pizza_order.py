print("Welcome to Python Pizza Deliveries");

bill = 0;

size_S = 15;
size_M = 20;
size_L = 25;
pepperoni_S = 2;
pepperoni_ML = 3;
cheese = 1;

size = input("what size pizza do you want ? \n S/M/L(small/medium/large) :")
add_pepperoni = input("Do you want to add pepperoni? \n Y/N(yes/no) :");
extra_cheese = input("Do you want extra cheese ? \n Y/N(yes/no) :");

if (size == "S"):
    bill += size_S;
    if(add_pepperoni == "Y"):
        bill += pepperoni_S;
        if(extra_cheese == "Y"):
            bill += cheese;
if (size == "M"):
    bill += size_M;
    if(add_pepperoni == "Y"):
        bill += pepperoni_ML;
        if(extra_cheese == "Y"):
            bill += cheese;

if (size == "L"):
    bill += size_L;
    if(add_pepperoni == "Y"):
        bill += pepperoni_ML;
        if(extra_cheese == "Y"):
            bill += cheese;

print(f"your final bill is ${bill}");

