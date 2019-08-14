 # First thing to keep in mind. If a number B is dividable by another A
# there will be no remainder, in other world the remainder must be zero
for i in range(1,101,1):           # Use for loop to count from 1-100, in the argument the first number is 
                                   # the starting point the second is the number of count normally count also zero
                                   # the last one is the increment step
    if i % 15 == 0:                # I have used the if statement to check the condition  
        print ('FizzBuzz',end=',') # I have used end=',' to display the output in a line 
    elif i % 5 == 0:
        print ('Buzz',end=',')
    elif i % 3 == 0:               # It is very important to check the condition of 15 first then the other two numbers
                                   
        print ('Fizz',end=',')     
    else :
        print (i,end=',')          
