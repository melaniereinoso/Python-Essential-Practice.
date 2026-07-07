for i in range(5,26):
    print(i)

for i in range(30,-1,-3):
    print(i)

number=int(input("Escriba un numero"))

for i in range (1, number+1):
    print(i)




#break
while True:
    word= input("Enter a word or type 'chupacabra' to exit")
    if word == "chupacabra":
        break
print("You've successfully left the loop.")



#continue  
# Prompt the user to enter a word
user_word = input("Enter a word")
# and assign it to the user_word variable.

for letter in user_word:
    # Complete the body of the for loop.
  
   if letter == "e":
       continue
   print(letter)    



blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1


ladrillo = int(input("Enter the number of blocks: ")) # ask user a number of blocks
steps= 0 #steps that we have gone already
needed= 2# steps we need to go 

while ladrillo >= needed:
    ladrillo -= needed #decrementing the steps that we need to go.
    steps +=1 #incrementing the steps we have gone already
    needed += 1 #incrementing the steps that we need to go on the next layer. 

print("the steps needed were: ", steps)



ladrillo = int(input("Enter the number of blocks you have: ")) # ask user a number of blocks
steps= 0 #steps that we have gone already
needed= int(input("How many steps should we go: "))#were we will start

while ladrillo >= needed:
    ladrillo -= needed #decrementing the steps that we need to go.
    steps +=1 #incrementing the steps we have gone already
    needed += 1 #incrementing the steps that we need to go on the next layer. 

print("the steps needed were: ", steps)




    

email = "john.smith@pythoninstitute.org"

for letter in email:
    if letter == "@":
        break
    print(letter, end=" ")
