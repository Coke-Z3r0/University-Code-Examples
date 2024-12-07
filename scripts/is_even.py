def is_even(number):
    if number % 2 ==0:#if the number when divided by 2 leaves a remainder, it is odd
        result=True
    else:
        result=False
    return result
    

if __name__ == "__main__":
#Test 1
    expected=True
    result = is_even(12)#testing with an even number
    if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")

#Test 2
    expected=False
    result = is_even(9)#testing with an odd number
    if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")
        
#Test 3
    expected=True
    result = is_even(-6)#testing with a negative even number
    if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
