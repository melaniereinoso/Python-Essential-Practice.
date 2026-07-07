#To make such decisions, Python offers a special instruction. Due to its nature and its application, it's called a conditional instruction (or conditional statement).

#if true_or_not:
    #do_this_if_true

#How does that statement work?

#If the true_or_not expression represents the truth (i.e., its value is not equal to zero), the indented statement(s) will be executed;
#if the true_or_not expression does not represent the truth (i.e., its value is equal to zero), the indented statement(s) will be omitted (ignored), and the next executed instruction will be the one after the original indentation level.

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))


if number1 > number2 and number1 > number3:
    largest_number = number1
elif number2 > number1 and number2> number3:
    largest_number= number2
else:
    largest_number = number3

print ("The larger mumber is " + str(largest_number))

# TAX calculator 
income = float(input("Enter the annual income: "))

if income > 1 and income < 85528:
	tax = income * 0.18 - 556.02
# Write the rest of your code here.
elif income == 0:
    tax = 0
else:
    tax = (income - 85528) * 0.32 + 14839.02


tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#identify the year program

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # If the year isn't divisible by 4, it's a common year.
    if year % 4 != 0:
        print("common year")
    # If it's divisible by 4 but not by 100, it's a leap year.
    elif year % 100 != 0:
        print("leap year")
    # If it's divisible by 100 but not by 400, it's a common year.
    elif year % 400 != 0:
        print("common year")
    # Otherwise, it's a leap year.
    else:
        print("leap year")      


    