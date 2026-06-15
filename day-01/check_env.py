# get the environmet fron User and print it
env=input("enter the environment") # taking input from the user 
print(env) 

# conditional statement
if env == "prod":
    print("Don't Deploy on Friday") 
elif env == "stag":
    print("take backup and test")    
else:
    print("safe to deploy on anyday")    

a= int(input("Enter the first number")) # typecasting
b=int(input("Enter the second number")) 
print(type(a))
print(type(b))


print("Multiplication is:",a*b)
print("Addition is:",a+b)
print("Multiplication is:",a-b)
print("Dividation is:",a/b)


