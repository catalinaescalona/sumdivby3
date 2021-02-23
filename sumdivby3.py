#This is a program that takes any integer and returns if it is divisible by 3

x_string = input("Enter a number to check if it's divisible by 3:") #Prompt the user to enter in a number

x_list = list(x_string) #Turn the characters of the input string into a list

x_sum = 0 #Initialize an accumulator

for num in x_list:
    x_sum += int(num) #Use accumulator pattern to take sum of digits from input list

if x_sum < 10: #Check if x_sum value is a single integer less than 10
    if x_sum == 3 or x_sum == 6 or x_sum == 9: #If single integer is 3, 6, or 9, then yes, div by 3
        print("Yes, it is divisible by 3.")
    else:
        print("No, it is not divisible by 3.") #If single integer not 3, 6, or 9, AND less than 10, then no, not div by 3

y_sum = 0 #initialize another accumulator if x_sum was larger than than a single integer

if x_sum >= 10: #Check if x_sum value was larger than a single integer
    for num in str(x_sum): #Iterate over the characters of the string of x_sum
        y_sum += int(num) #Use accumulator pattern to take sum of digits of x_sum

if y_sum < 10: #Check if y_sum value is a single integer less than 10
    if y_sum == 3 or y_sum == 6 or y_sum == 9: #If single integer is 3, 6, or 9, then yes, div by 3
        print("Yes, it is divisible by 3.")
    else:
        print("No, it is not divisible by 3.") #If single integer not 3, 6, or 9, AND less than 10, then no, not div by 3
