print("Welcome to the tip calculator. ");
total = input("What was the total bill ?\n");
percentage = input("What percentage tip would you like to give ? 10, 12 or 15?\n");
people = input("How many people to split the bill?\n");

total_cost = float(total) * (1 + (float(percentage) * 0.01));

each_person = round(total_cost / float(people), 2);
each_person_2 = "{:.2f}".format(round(total_cost / float(people), 2));

print(f"each person should pay: ${each_person}")
print(f"each person should pay: ${each_person_2}")




"""
Welcome to the tip calculator.
What was the total bill ?
150
What percentage tip would you like to give ? 10, 12 or 15?
12
How many people to split the bill?
5
each person should pay: $33.6
each person should pay: $33.60
"""
