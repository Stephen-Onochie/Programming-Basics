"""
This simple script converts a temperature in celsius to fahrenheit
"""

def convertToF(celsius):
    #calculates the temp in fahrenheit
    fahrenheit = int(celsius) * (9/5) + 32
    return "The temperature is " + str(fahrenheit) + " degrees in fahrenheit"

#gets celsius temp and runs function
print(convertToF(input("How hot is it? (C) => ")))