
# Discussion Assignment Unit 5 CS 1101

## Part 1:

This version of the algorithm checks every character (c) of a given string (s) if it is lowercase or not. When .islower() is called on a character that is a lowercase letter it evaluates to true and returns True. Since the else statement with a return, the statement is right after when the first iteration of the loop begins it will always result in a return statement causing the function to be pushed off the call stack and no other letter except the first to ever be seen by the for loop. In order to fix this all you have to do is get rid of the else statement and move the return False statement to the end of the function outside of the loop. This way it checks every character in the string and returns the bool True if it finds a lowercase letter, and if it never does then it just finishes the loop and returns the bool False.

## Part 2:

This version is very similar to the previous, there are only three differences, the return values are strings and c is being referenced as a string instead of a variable. This function will behave in a similar way except for a few differences as well, it can also be solved in a similar manner. If you want you can change the string return values to bools, but you don't need to since there isn't anything saying bool return value is required. Now for the bigger issue, when .islower() is called on 'c', it is always called on 'c', a string, and it will never check the string passed in as an argument. This way it always evaluates to 'True', since it is a lowercase character. If you get rid of the quotes around 'c', then it is solved, and all that's needed is to follow the instructions in Part 1 of this post.

## Part 3:

I don't know why this function works, but it does, not properly but it shouldn't be able to run at all. In this function, the variable flag is initialized in a loop, therefore by the time the loop is finished the variable should be deleted by the Python garbage collection system, and is out of scope. Other than that lies the issue with reassignment. Every time the function runs it reassigns flag to the bool result of the current character being passed through .islower(). Since it does this with every character, the result of the function is always dependent upon whether or not the last character in the string is a lowercase letter or not. Therefore it will always forget if there were any previous uppercase characters in the string by the time it reaches the end of it. In order to fix this, you would need to create an if statement that checks if c.islower() evaluates to true, and only then will it change the value of flag. This way it can't change the value of flag after it sees an uppercase character and return the wrong value. You should also initialize flag before the for loop

## Part 4:

This version works just fine. Here the flag variable is set properly outside the loop with the value of False. Every time the loop checks a character it sets it's value to true if it is already true or true if c.islower() evaluates to true, and False otherwise. Then it returns the correct bool value.

## Part 5:

A similar issue to the first one. Here if, not c.islower(), ever evaluates to true, the function returns. Son of there are any uppercase letters in the string at all it will exit the function, regardless of the presence of lowercase letters. I can't figure out a way to refactor this without rewriting the logic completely. You can't check for the inverse of something and then follow that up with a return statement if it happens to evaluate to true. If anyone knows how to make this work without significant refactoring, I would like to know.