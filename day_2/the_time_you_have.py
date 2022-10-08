# Assum you can live to 90 years old

current_age = input("what's your current age ? \n");
left_years = 90 - int(current_age);

days = 365 * left_years
weeks = 52 * left_years
months = 12 * left_years

print(f"you have {days} days, {weeks} weeks, and {months} months left");
