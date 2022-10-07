#
# String
#

print("Hello");



#
# String can be accessed as a array using indexing
#

print("Hello"[0]);
print("Hello"[1]);
print("Hello"[2]);
print("Hello"[3]);
print("Hello"[4]);
# print("Hello"[5]);    # error



#
# integer
#
print("123" + "456" )
print(123 + 456)


#
# float
#
print(3.1415926)



#
# boolean
#
# print(true)       
# print(false)
# 
print(True)     # Captical
print(False)




#
# type checking 
#
print(type("what's your name"));
print(type(123));
print(type(3.1415926));
print(type(True));

# checking function's return value's data type
print(type(len("hello")));





#
# type casting 
#
number_of_string = len("hello");
print(type(number_of_string));

print("Converting to string")
print(type(str(number_of_string)));

print("Converting to float")
print(type(float(number_of_string)));


