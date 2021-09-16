# Define a function to account for early escapes
def calc():
    # Get user input
    u = input("heb je een U? Zo ja voer m dan ff, zo nee skip dan maar: ")
    i = input("heb je een I? Zo ja voer m dan ff, zo nee skip dan maar: ")
    r = input("heb je een R? Zo ja voer m dan ff, zo nee skip dan maar: ")

    # Get the lengths of the input variables respectively
    lenI = len(i)
    lenU = len(u)
    lenR = len(r)

    # Check if input is numeric where it should be (e.g. length == 0 is empty string, could be valid)
    if((not u.isnumeric() and lenU != 0) or (not i.isnumeric() and lenI != 0) or (not r.isnumeric() and lenR != 0)):
        print('Ik kan alleen werken met getallen.') # Print error
        return # Early escape

    # Validate length combinations
    if((lenU == 0 and lenI == 0) or (lenU == 0 and lenR == 0) or (lenI == 0 and lenR == 0)):
        print('Onvoldoende informatie') # Print error
        return # Early escape

    # Calculate and print the values
    # Print calculated value if component input was not empty
    print(int(i) * int(r) if lenU == 0 else u)
    print(int(u) / int(r) if lenI == 0 else i)
    print(int(u) / int(i) if lenR == 0 else r)

calc()