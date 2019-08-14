string = input(str("Enter a string here: ")) # Getting a string from the user
def reverse(string):                         # defining a function
  str = ""                                   # 
  for i in string:                           # Using the loop to define every sing element of the string
    str = i + str                            # Calling the function to iterate every element and join them 
  return str
print ("Your reversed string here: ",reverse(string))
  
