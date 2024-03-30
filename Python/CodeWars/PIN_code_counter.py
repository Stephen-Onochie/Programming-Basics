# TM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

#solved
def validate_pin(pin):
    #checks if pin length is 4 or 6 and pin is only digits
    return True if (len(pin) == 4 and pin.isdigit()) or (len(pin) == 6 and pin.isdigit()) else False