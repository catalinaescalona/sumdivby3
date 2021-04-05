#ASSIGNMENT: Using only the rule that the sum of the digits of a number must be divisible by 3
#for the integer to be divisible by 3, write RECURSIVE Python code for a function
#that takes an integer and returns whether it is divisible by 3 or not


#A recursive function to calculate the sum of each individual number using mod
#Intended as more "under the hood" to be used within the divby3 function
def sumofnum(num): #takes the input of the number
    if num == 0:
        return 0 #if the number is 0, return 0
    else:
        last_digit = num % 10 #find the last digit of num
        num = num // 10 #reassign value of num, now it is every number in previous num excluding the last digit
        total = last_digit + sumofnum(num) #add the last digit to the sum of the remaining numbers in num
        return total #return the sum of digits (continue recursively until numbers are all summed together)

#A function to check if the input number is divisible by 3
def divby3(num):
    value = sumofnum(num) #call the sumofnum function to recursively add each number together
    if value % 3 == 0: #check if the value is divisible by 3
        return "Yes, it is divisible by 3." #If yes, return yes
    return "No, it is not divisible by 3." #If no, return no

user_input = input("Enter a number to check if it's divisible by 3: ") #user enteres in a number, which is stored as a string
user_num = int(user_input) #string is converted into integer

print("The sum of the numbers is: ", sumofnum(user_num)) #print out the sum of the numbers
print(divby3(user_num)) #print out whether the number is divisible by 3 or not
