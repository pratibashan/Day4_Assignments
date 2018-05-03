
user_number = int(input("Enter the Number : "))



if user_number > 2:
    for i in range(2, user_number):
        if (user_number % i == 0):
            print(f" Number {user_number} is not a prime number")
            break
    else:
        print(f" Number {user_number} is a prime number")     

else:

    print(f" Number is not a prime number.")        

   

