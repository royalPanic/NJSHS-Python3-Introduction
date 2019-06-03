def square_digits(num): # first we make a function that accepts an integer as a input
    chars = list(str(num)) # next, we take the input of num, which is a integer, and we cast it (change it) to a string with str(). we then cast it again to a list, which will generate a list of the characters in the string
    i = 0 # create a variable
    squares = [] # create an empty list
    for n in range(len(chars)): # n refers to the current iteration on the list. it repeats that for the length of the chars list
        squares.append(str(int(chars[i])*int(chars[i]))) # add the square of the number to the empty list
        i += 1
    return("".join(squares)) # join the list together as a string and return it as the result of the function
