fib_range = int(input("Enter your range here: "))
def fibionacci(): # from the mathematical formula F(n) equal 0 if n equal 0
                  # and F(n) equal 1 for n equal 1 and for n > 1 F(n) = Fn-1 + Fn-2
    a, b = 0, 1   # setting up the first two conditions, and declaring the variables
    while True:   # for the loop wile do the addition as long as the conditions will remain true 
        yield a            # yield forces the loop to start the count at 0
        a, b = b, a + b    # forcing a to equal b and adding a to b, or 1, (0 + 1) 
                           # this operation will then be applied to each element in the for loop
for element, n in zip(range(fib_range), fibionacci()): # very important to use the zip function as the values are too large to be unpacked 
     print('{i:3}: {f:3}'.format(i=element, f=n))  

