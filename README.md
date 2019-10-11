Welcome, I'm royal_Panic, and I wrote this guide to teach the fundamentals of Python to my classmates and potentially other classes down the line. There's really no substantial introduction to this, so let's jump right in.

## What is Python?
Python is a computer programming language designed to be powerful while also being as readable as possible to introduce newcomers. It is regarded as one of the best beginner programming languages, and despite often being portrayed as nothing but a simple beginners' language, it actually powers some incredibly well-known open and close-sourced programs.

## Some Notable Uses of Python:
* Google Drive
* Reddit
* Instagram
* Google Search
* The Spotify App
* Netflix
* Uber
* Dropbox

## Getting Started with Python:
### IDLE
Firstly, we're going to need to download and install Python to your computer. [(If you're not going to download Python, or you'd rather use an online compiler, start here.)](#replit) The basic Python interpreter/compiler is called **IDLE**, and it's available for free from the [official Python website](https://www.python.org/downloads/). Download the latest version of Python v3.x (v3.7.3 as of writing), and install it on your computer. After you're done, open IDLE. This will open to the "Python Terminal" window, but that's not what we want, so simply press `CTRL+N` to open a new `.py` document.

### REPL.IT
**Repl.it** is an online compiler and interpreter, and it allows us to write and test code in our browser with no downloads. To start, navigate to [Repl](https://repl.it/) and create an account. Then, make a new program, and select `Python3` as the language.

## Our First Program:
As is with standard programming tradition, our first program will be a simple "Hello world!" script. Doing this in python is incredibly simple, as we only have to print a string.

```python
print("Hello world!")
```
That's it! That's all! Very simple. Now, let's move on to some of the fundamentals of Python.

## Variables:
Variables are objects in code that can be set to have a certain value, and we can later change or compare that value.

### Types of Variables:
There are 5 basic types of variables in python, we'll only be working substantially with 3 of them in this document.

```python
string = "string"
integer = 5
list = [1,"Two",3]
tuple = ("one", 2, "three")
dictionary = {"fruit": "apple", "brick": "red"}
```
A **String** is a basic variable that contains any character, it's defined by surrounding text with double or single quotes. **Integers** are whole numbers, negative or positive, with no decimal value. A **List** is a changeable, indexed (ordered) set of other variables (including other lists!). While a **Tuple** is an unchangeable, un-indexed set of variables. Finally, a **Dictionary** is a set of variables where a relationship is defined. This allows us to call the "key" (the first corresponding value in the dictionary) and return the corresponding value.

## Loops:
Loops are blocks of code that allow us to repeat sections of code for a predefined amount of times, or until a condition is met.

### Types of Loops
There are 4 basic types of loop in python, and they are triggered and repeated by varying conditions.

```python
x = 1
list = [1, 2, 3]
while x == 1: # at all times when x = 1, this loop will run
    print("Hello world!")

if x == 1: # this loop checks to see if the condition is met, and if it is, it runs
    print("Hello world!")

for y in list: # this loop runs the code for every instance of a value in an iterable
    print("Hello world!")
```

A **while loop** continues to run as long as its condition is fulfilled. A **for loop** iterates through a special kind of variable called an iterable. The only iterable variable type we'll we working with in this guide is a list. An **if loop** checks the condition, and if it is true, it runs the code, if not, it doesn't. *If* loops are especially important because they can be extended past their standard form. While an *if* loop starts with `if`, it can be extended perpetually with `elif` (else/if) and `else`. For instance:

```python
x = 4

if x == 1:
    print("x = 1")
elif x == 3:
    print("x = 3")
else:
    print("x doesn't equal 1 or 3")
```

### Loop Logical Modifiers:
Say you don't just want to check one thing, no worries, all your favourite standard logic gates exist within python loops. This allows us to check multiple conditions at once to further specify when loops should run as opposed to nesting *if* loops until we get to where we need. The most commonly used logical modifiers are `AND` and `OR`, but there are others. To see them in use, let's see two ways of making the same conditional loop.

```python
x = 1
y = 2

if x == 1:
    if y == 2:
        print("All conditions are met.")
```

Now, this isn't really readable or very efficient, so let's see the same loop created with logical modifiers.

```python
x = 1
y = 2

if x == 1 and y == 2:
    print("All conditions are met.")
```

Now before we get to the first challenge, let's review one more key feature of python.

## Functions:
Functions are ever present in python, they make up every command you use, whether you know it or not. The main function we've been using up until now is `print()`. However, we can easily define our own functions in python, and even give them custom arguments.

```python
def myFunction(input):
    print(str(input))
```

This function will print whatever we give it as an argument. Running this will give us the result of our function.

```python
myFunction("apple pi")
```

Will return:

```
>>> "apple pi"
```

Now that we've conquered the fundamentals of python, let's start with a basic challenge to see what you've learned.

## Challenge 1 - Square Digits:
>Welcome. You have been asked to square every digit of a number. For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Since this is the first challenge, I'll walk through how to solve it, and introduce you to variable casting.

```python
def square_digits(num): # first we make a function that accepts an integer as a input
    chars = list(str(num)) # next, we take the input of num, which is a integer, and we cast it (change it) to a string with str(). we then cast it again to a list, which will generate a list of the characters in the string
    i = 0 # create a variable
    squares = [] # create an empty list
    for n in range(len(chars)): # n refers to the current iteration on the list. it repeats that for the length of the chars list
        squares.append(str(int(chars[i])*int(chars[i]))) # add the square of the number to the empty list
        i += 1
    return("".join(squares)) # join the list together as a string and return it as the result of the function
```

## Iterables and the *For* Loop:
So while we already looked at the *For* loop as an easy way to move through a iterable-type variable. Now we're going to further explore this, and how we can use it to make several iterations of the same loop.

```python
list = [1,"two", 3]

for x in list: # here we assign x as a (hyper)local variable, where x is defined as the current iteration of the list, which we move through in the loop
    print(x)
```

The above will return us:

```
>>> 1
>>> "two" # it may also just return `two` instead of `"two"` depending on your compiler
>>> 3
```
