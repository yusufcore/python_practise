name = input("Enter your name please: ")
age = input("Enter your age please: ")
print("Hello", name)
print("Your age is", age)

print(type(name))
print(type(age))    # input function always returns a string value, so the type of age will also be string.    

a = 13
b = 67

print(f"The sum is {a + b}")