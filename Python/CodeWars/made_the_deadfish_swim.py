# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]

#passed - learned to use n1 ** n2 intead of math.pow(n1,n2) for large numbers
import math
def parse(data):
    # TODO: your code here
    result = []
    value = 0
    for char in data:
        match(char):
            case 'i':
                value+=1
            case 'd':
                value-=1
            case 's':
                value = value ** 2
            case 'o':
                result.append(value)
                
    return result