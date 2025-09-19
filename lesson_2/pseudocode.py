# a function that returns the sum of two numbers

SET num1
SET num2
PRINT num 1 + num 2

# a function that takes a list of strings, and returns a string that is all those strings concatenated together
GET []
FOR item in []
    PRINT STRING


a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance:

every_other([1,4,7,2,5]) # => [1,7,5]

GET []
SET ITERATOR = 0
FOR item in []
    PRINT item
    ITERATOR + 2

# a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.

SET given_char
SET count = 0
IF char == given_char
    count =+ 1

IF count <= 3
    PRINT count
ELSE
    None

