print("Welcome to love caculator !");
name1 = input("what's your name ?\n");
name2 = input("what's their name ?\n");


# convert the names to lowercases 
name1_l = name1.lower();
name2_l = name2.lower();

# get how many time the "TRUE"  have been occured in names
t = name1_l.count('t') + name2_l.count('t');
r = name1_l.count('r') + name2_l.count('r');
u = name1_l.count('u') + name2_l.count('u');
e = name1_l.count('e') + name2_l.count('e');

true = t+r+u+e;


# get how many time the "LOVE"  have been occured in names
l = name1_l.count('l') + name2_l.count('l');
o = name1_l.count('o') + name2_l.count('o');
v = name1_l.count('v') + name2_l.count('v');
e = name1_l.count('e') + name2_l.count('e');

love = l+o+v+e
love_score = true * 10 + love;

print(true);
print(love);
print(f"Your love score is {love_score}");


if (love_score > 90 or love_score <10):
    print(f"Your love score is {love_score}, you should go together like coke and mentos");

if (love_score > 40 and love_score <50):
    print(f"Your love score is {love_score}, you are alright together.");

if ((love_score >= 10 and love_score <=40 ) or (love_score >= 50 and love_score <=90 )):
    print(f"Your love score is {love_score}.");

