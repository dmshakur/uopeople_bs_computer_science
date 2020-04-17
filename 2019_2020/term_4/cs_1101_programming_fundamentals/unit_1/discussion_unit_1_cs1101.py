
#                                      #
# Discussion Assignment Unit 1 CS_1101 #
#                                      #

# print('Hello World!') # RESULT: Hello World!
#### Explanation ####
# print() is a function in Python that by default is included with Python Version 3. 
# In previous versions of python it work a little differently with the parentheses not being present. 
# It is very useful and can be customized a great deal with formatted strings and arguments such as sep and end. 
# sep takes a string as an argument to use to separate all the variables passed through the function, 
# end just changes the character placed after all your values, which is new line by default, or '\n' in C++.
# > Resources:
    #  docs.python.org/3/whatsnew/3.0.html,
    #  previous knowledge of C++

# print(1/2) # RESULT: 0.5
#### Explanation ####
# A simple division operation, 1 divided by 2 results in 0.5. 
# No functions are being used to display the output and the output is not being saved to any variable therefore it is not available for further use. 
# But useful if you just need to know what 1 / 2 is. Side note the operation is on two integers and the output is a float.

# print(type(1/2)) # RESULT: <class 'float'>
#### Explanation ####
# Here we are passing two numbers into a function being divided. 
# The function registers and returns the type of the variable sent in. 
# However what really happens is the division operation takes place before anything is sent in to the function type, 
# so type() is will output the type of the float 0.5 instead of either number, the operator or the operation.

# print(01) # RESULT: SyntaxError: invalid token
#### Explanation ####
# The print function is being called with 01 as an argument, the execution of this function results in an error as leading zeros are not allowed in Python. 
# Now I have not been able to find any supporting documentation for my theory but I will type it out anyways. 
# I believe what is happening is the interpreter is seeing the zero with no period after it and saying 'okay I have the number 0 here', then it looks at the second number, 1. 
# I believe that this is the same as print(0 1), where no operation is being performed and two values are being sent into a function as one argument.

# print(1/(2/3)) # RESULT: 1.5
#### Explanation ####
# Here we have simple arithmetic. The interpreter sees 1 then / so it divides 1 by the following value. 
# After the first / the interpreter sees parentheses with another division operation taking place. 
# Using parentheses makes sure that the operation inside takes place and the returned value is used as an argument for the first division operation. 
# With the parentheses 1 is divided by the result of 2 /3. 
# Without the parentheses 1 would divide by 2 and the result of that operation would be divided by 3, resulting in 0.16 a much smaller number
