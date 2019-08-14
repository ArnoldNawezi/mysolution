num1 = int (input("Enter your num here: "))  # Getting from the user the number to be multiply
start = int (input("From which number you want to start your multiplication: ")) # Getting from the user the starting number for the multiplication
num2 = int (input("Up to which number you want to multiply: ")) #
n = num2 + 1 # Setting the number of count to be use in the loop
for i in range (start,n): # Using for loop to repeat the multiplication n times
    print (num1,'x',i,'=',num1*i) # Output
