
# Python Lists Exercise: Replace Middle Element, Remove Last Item, and Get List Length

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

hat_list[2] = int(input("Write a number")) # Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

del(hat_list[-1])# Step 2: write a line of code that removes the last element from the list.

print(len(hat_list))# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)


#A new element may be glued to the end of the existing list:
#list.append(value)
#Such an operation is performed by a method named append(). It takes its argument's value and puts it at the end of the list which owns the method.

#.append()- to add an ellement at the end of the list

#The insert() method is a bit smarter ‒ it can add a new element at any place in the list, not only at the end.
#list.insert(location, value)
 
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)


##########################################

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#############################
my_list = [10, 1, 8, 3, 5]  # Initial list of numbers

total = 0  # Variable to store the sum of all elements

for i in range(len(my_list)):  
    # Loop through the list using indexes (from 0 to len-1)

    total += my_list[i]  
    # Add the current element of the list to total

print(total)  
# Print the final sum of all elements in the list


#############################################
# Step 1: Create an empty list called 'beatles'
beatles = []

# Step 2: Add initial members to the list using append()
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Step 3: Use a loop and input() to add two more members to the list
# (Stu Sutcliffe and Pete Best)
for i in range(2):
    beatles.append(input("Add a member: "))

# Step 4: Remove Stu Sutcliffe and Pete Best from the list
del beatles[3:]

# Step 5: Add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")

# Final step: print the length of the list
print("The Fab:", len(beatles))



# Create a list containing integer numbers.

# Loop through the list using enumerate()
# so you can access both the position (index) and the value of each element.

# Check if the current value is greater than 5.

# If the value is greater than 5,
# replace that element in the list with 0 using its index.

# After checking all elements,
# print the updated list.

numbers = [3, 7, 2, 9, 4, 6]

for i, elem in enumerate(numbers):
    if elem > 5:
        numbers[i] = 0

print(numbers)



# Exercise 1: Accessing list elements, negative indexes, length, and searching in a list

numbero = [7, 3, 9, 1, 5]

# Print the first element of the list using index 0
print(numbero[0])

# Print the last element of the list using negative indexing
print(numbero[-1])

# Print the number of elements inside the list
print(len(numbero))

# Loop through each element in the list
for i in numbero:
    # Check if the current element is equal to 9
    if i == 9:
        # Print a message when 9 is found
        print(i, "is in the list")



# Exercise 2: Filtering values from a list using a condition

numero = [12, 5, 18, 3, 21, 8]

# Loop through each number in the list
for i in numero:
    # Print only numbers greater than 9
    if i > 9:
        print(i)



# Exercise 3: Modifying list elements using enumerate()

numbers = [2, 9, 4, 11, 6, 15]

# enumerate() gives both the index and the value of each element
for i, elem in enumerate(numbers):
    # Check if the current number is odd
    if elem % 2 == 1:
        # Replace odd numbers with 0 using the index
        numbers[i] = 0

# Print the modified list
print(numbers)



# Exercise 4: Traversing a list backwards using range()

numbers = [10, 20, 30, 40, 50]

# range(start, stop, step)
# Start from the last index, stop before -1, and move backwards by -1
for i in range(len(numbers) - 1, -1, -1):
    # Print each element from the end to the beginning
    print(numbers[i])



# Exercise 5: Finding the largest number without using max()

numbers = [18, 4, 27, 11, 35, 9]

# Assume the first element is the largest initially
largestNumber = numbers[0]

# Start looping from the second element
for i in range(1, len(numbers)):
    # Compare the current element with the largest number found
    if numbers[i] > largestNumber:
        # Update largestNumber when a bigger value is found
        largestNumber = numbers[i]

# Print the largest number
print(largestNumber)



# Exercise 6: Creating a new list with values that meet a condition

numbers = [4, 15, 2, 20, 7, 30, 1]

# Create an empty list to store numbers greater than 10
greater_numbers = []

# Loop using indexes
for i in range(len(numbers)):
    # Check if the current number is greater than 10
    if numbers[i] > 10:
        # Add the number to the new list
        greater_numbers.append(numbers[i])



# Exercise 7: Counting elements that meet a condition

numbers = [5, 12, 7, 20, 3, 18, 9]

# Variable to store the amount of numbers greater than 10
count = 0

# Loop through each element in the list
for i in numbers:
    # Check if the number is greater than 10
    if i > 10:
        # Increase the counter by 1
        count += 1

# Print the total count
print("there are", count, "numbers greater than 10")



# Exercise 8: Modifying even numbers in the original list

numbers = [3, 6, 9, 12, 15]

# enumerate() provides the index and value
for i, number in enumerate(numbers):
    # Check if the number is even
    if number % 2 == 0:
        # Multiply the number by 2
        number *= 2

        # Update the original list using the index
        numbers[i] = number



# Exercise 9: Creating a new list with even numbers

numbers = [4, 7, 10, 13, 16, 19]

# Create an empty list to store even numbers
even_numbers = []

# Loop using enumerate to get index and value
for i, number in enumerate(numbers):
    # Check if the number is even
    if number % 2 == 0:
        # Add the even number to the new list
        even_numbers.append(numbers[i])

# Print the new list
print(even_numbers)

# listas dentro de listas

board = []

for i in range(2):
    row = []

    # Completa aquí el for que crea una fila de 4 ceros
    for j in range(4):
    # Agrega la fila al tablero
        row.append(0)

print(board)


classroom = []
for i in range(3):
    row = []
# Escribe tu código aquí
    for j in range(2):
    # Agrega la fila al tablero
        row.append("0")

print(classroom)
