def is_strong_password(password):
    if len (password) <8: #automatically returns false if password is less than 8 characters
        strong = False
    
    #setting up the Variables to search for
    has_upper= False
    has_lower=False
    has_digit=False
    has_special=False
    #Stating the special characters to search for
    special_characters = "!@#$%^&*()"
    
    for char in password:
        if char.isupper():#Checking for an Uppercase Letter
            has_upper=True
        elif char.islower():#Checking for a Lowercase Letter
            has_lower=True
        elif char.isdigit():#Checking for a digit
            has_digit=True
        elif char in special_characters:#Checking for a special character from the previous list
            has_special=True
    if has_upper and has_lower and has_digit and has_special:
        strong = True
    else:
        strong = False
    return strong

if __name__ == "__main__":
#Test 1
    expected=True # Result should be true(Strong Password)
    strong= is_strong_password('$trongPassword1')
    if strong == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {strong}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {strong}")
        
#Test 2
    expected=False # Result should be false(weak password, missing special character)
    strong= is_strong_password('weakPassword1')
    if strong == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {strong}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {strong}")


#Test 3
    expected=False # Result should be false(weak password, shorter than 8 characters)
    strong= is_strong_password('short')
    if strong == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {strong}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {strong}")
        

