
#Finding a factorial of a given no.

user_number =int(input("Enter a number to find the factorial value: "))

factorial =  1

for index in range(1,(user_number+1)):
    factorial *= index
    
print (f"The factorial value of a given number is {factorial}")    