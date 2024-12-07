def is_monotonic(string_of_digits):
    if len(string_of_digits) <= 1:#Checking if the Entered digits are Less that 1 value
        return True
    
    increasing = decreasing = True
    
    # Check for increasing and decreasing conditions
    for i in range(1, len(string_of_digits)):
        if string_of_digits[i] > string_of_digits[i-1]:
            decreasing = False
        elif string_of_digits[i] < string_of_digits[i-1]:
            increasing = False
        else:
            increasing=decreasing=True
    
    return increasing or decreasing
        
        

if __name__ == "__main__":
#Test 1
    expected=True # Result should be true(Monotonically increasing)
    increasing=decreasing = is_monotonic('22456')#testing with a string of increasing numbers
    if increasing or decreasing == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {increasing or decreasing}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {increasing or decreasing}")

#Test 2
    expected=True # Result should be true(Monotonically decreasing)
    increasing=decreasing = is_monotonic('66521')#testing with a string of decreasing numbers
    if increasing or decreasing == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {increasing or decreasing}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {increasing or decreasing}")
    
#Test 3
    expected=False # Result should be False(Non-Monotonic)
    increasing=decreasing = is_monotonic('98612')#testing with a string of non-monotonic numbers
    if increasing or decreasing == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {increasing or decreasing}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {increasing or decreasing}")


