print(3 + 4);
print(3 - 4);
print(3 * 4);
print(3 / 4);
print(3 ** 1);      # 3 
print(3 ** 2);      # 3 * 3
print(3 ** 3);      # 3 * 3 * 3
print(3 ** 4);      # 3 * 3 * 3 * 3
print(3 // 4);      # ??

print(3 * 3 + 3 / 3 - 3);           # (3*3) + (3/3) - 3 = 9 + 1 - 3 = 7
print(type(3 * 3 + 3 / 3 - 3));

#
# How to get just 7 instead of 7.0
#
print(int(3 * 3 + 3 / 3 - 3));           
print(type(int(3 * 3 + 3 / 3 - 3)));


#
# change the order using ()
#
print(3 * (3 + 3) / 3 - 3);
