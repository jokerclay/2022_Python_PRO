#
# Check if it is a leap year
# leap year caculation:
#   https://stackoverflow.com/questions/725098/leap-year-calculation
#

year = float(input("enter the year \n"));

if (year % 4 == 0 and year % 100 != 0):
    print("Leap year");

elif(year % 400 == 0):
    print("Leap year");

else:
    print("Not Leap year");


