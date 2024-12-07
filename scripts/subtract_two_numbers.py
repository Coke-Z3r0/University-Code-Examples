def subtract_two_numbers(m, n):

    result=m-n#subtracting the 2 numbers provided
    
    return result

if __name__ == "__main__":
#Test 1
    expected=6 # Result should be 6
    result= subtract_two_numbers(10,4)#testing for subtracting 2 positive numbers
    if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")

#Test 2
    expected=-10 # Result should be -10
    result= subtract_two_numbers(-6,4)#testing for subtracting 1 positive and 1 negative number
    if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")
        
#Test 3
    expected=5 # Result should be 5
    result= subtract_two_numbers(-5,-10)#testing for subtracting 2 negative numbers
    if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
