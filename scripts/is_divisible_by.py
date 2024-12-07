def is_divisible_by(number, denominators):
    for denom in denominators:
        if number % denom !=0:#checking to see if when the number is divided, there is no remainder
            valid=False
        else: 
            valid=True
    return valid

if __name__ == "__main__":
#Test 1
    expected=True
    valid = is_divisible_by(12,[3,4])#testing with numbers that divide equally
    if valid == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {valid}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {valid}")
        
#Test 1
    expected=False
    valid = is_divisible_by(17,[3,9])#testing with numbers that dont divide equally
    if valid == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {valid}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {valid}")
        
#Test 3
    expected=True
    valid = is_divisible_by(-12,[-4,3])#testing with negative numbers that go into each other equally 
    if valid == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {valid}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {valid}")
