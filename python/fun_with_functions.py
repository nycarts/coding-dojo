'''
Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

Your program output should look like below:

Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.

'''

def odd_even():

  for i in range(1, 2001):
    if i % 2 != 0:
      print('Number is {}.  This is an odd number.'.format(i))
    else:
      print('Number is {}.  This is an even number.'.format(i))

odd_even()

'''

Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:

a = [2,4,10,16]

Then:

b = multiply(a, 5)
print b

Should print [10, 20, 50, 80 ].

'''

def multiply(listy):

  new_listy = []

  for i in listy:
    new_listy.append(i * 5)

  print new_listy


multiply([2, 4, 10, 16])

'''

Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list. Here's an example:

def layered_multiples(arr)
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

'''

# def layered_multiples(listy):

#  for i in 

# x = layered_multiples(multiply([2, 4, 5], 3))
# print x


  