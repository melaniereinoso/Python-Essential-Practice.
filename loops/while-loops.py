#while-loop
# Store the current largest number here.
largest_number = -999999999
 
# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))
 
# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))
 
# Print the largest number.
print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
 
odd_numbers = 0
even_numbers = 0
 
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
 
# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
 
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


# to get out of the loop

counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# the number will be decrementing by 1 so once it gets to 0 it will stop the loop.


counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)
 
 #El loop se ejecuta porque el valor de la variable es 5, y en Python cualquier número distinto de 0 es considerado truthy (verdadero) en un contexto booleano.


count=3
attemptsUsed = 1
secret= 25

numero= int(input("Adivina el numero secreto. tienes 3 intentos"))

while numero != secret:
    print("Wrong! Try again.")
    count-=1
    attemptsUsed +=1
    print("You have" + str(count) + "left")
    if count == 0:
        print("No more attempts")
    else:
        numero= int(input("Adivina el numero secreto"))
     
else:
        print("Correct!")
        print("you used" + str(attemptsUsed - 1) + "attempts" )



#secret = 25
#Pedir un número al usuario.
#Mientras el número sea diferente del secreto:
#Mostrar "Wrong! Try again."
#Contar el intento.
#Pedir otro número.
#Cuando el usuario acierte:
#Mostrar "Correct!"
#Mostrar cuántos intentos necesitó.

count=1
secret= 25

numero= int(input("Adivina el numero secreto."))

while numero != secret:
    print("Wrong! Try again.")
    count+=1
    #print("You have" + str(count) + "left")
    numero= int(input("Adivina el numero secreto"))
     
else:
        print("Correct!")
        print("you used" + str(count ) + "attempts" )


#Ejercicio: Analizador de números ⭐⭐⭐⭐

#Crea un programa que haga lo siguiente:

#Pida números enteros al usuario.
#El usuario puede escribir tantos números como quiera.
#El programa termina cuando el usuario escriba 0.

#Mientras el programa está ejecutándose, debe:

#Contar cuántos números positivos se ingresaron.
#Contar cuántos números negativos se ingresaron.
#Contar cuántos números pares se ingresaron.
#Contar cuántos números impares se ingresaron.
#Calcular la suma de todos los números (sin incluir el 0).

numeros=int(input("Escriba un numero o escriba 0 para finalizar"))
sum= 0
evenNumbers= 0
oddNumbers= 0
positiveNumbers= 0
negativeNumbers= 0

while numeros !=0:
    sum += numeros
    if numeros % 2 != 0:
        oddNumbers+=1
        
    else:
        evenNumbers +=1
       
    if numeros > 0:
         positiveNumbers +=1
    else:
         negativeNumbers+=1
         
    numeros=int(input("Escriba un numero o escriba 0 para finalizar"))

print("la suma es",sum)
print("Positives are", positiveNumbers) 
print("Negatives are ", negativeNumbers)
print("Even numbers ", evenNumbers)
print("Odd numbers ", oddNumbers)
print("Juego finalizado")


# Collatz Conjecture - Python Essentials Practice
# This program reads a positive integer, applies the Collatz algorithm,
# displays each intermediate value, and counts the total number of steps
# required to reach 1.

c0= int(input("type a number"))
steps= 0

while c0 != 1:
    steps +=1
    if c0 %2 == 0:
        c0 =  c0//2
        print(c0)
    else:
        c0 = 3 * c0 +1
        print(c0)
print("The numbers of steps where: ",steps)   