#
# round() goes to the close integer 
#         & if it X.5, it goes 
#
#

print(3 / 1.6);
print(round(3 / 1.6));
print("=========================");

print(3 / 1.5);
print(round(3 / 1.5));
print("=========================");


print(3 / 1.3);
print(round(3 / 1.3));
print("=========================");


print(3 / 1.2);
print(round(3 / 1.2));
print("=========================");


print(3 / 1.15);
print(round(3 / 1.15));
print("=========================");

print(3 / 1.1);
print(round(3 / 1.1));
print("=========================");


print(3 / 1.1);
print(round(3 / 1.1, 2));           # save 2 numbers after the point
print("=========================");


print(3 // 2);                    # just get the integer part
print(type(3 // 2));

print(4 / 2);
print(type(4 / 2));               # even you get a 2, but still 2.0 as a float

print(4 // 2);
print(type(4 // 2));
print("=========================");

res = 4 / 2
res /= 2 
print(res);


score = 0;
score += 1;
print(score);
print(type(score));
print("your score is " + str(score));
print("=========================");


#
# f-String
#
my_score = 10;
height = 180;
isWinng  = True;
print(f"my score is {my_score} my height is {height} and I am Winning is {isWinng}");


