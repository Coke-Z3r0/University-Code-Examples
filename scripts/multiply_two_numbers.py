def multiply_two_numbers(m, n):

    result = m*n#calculating the result by multiplying the two numbers provided
    
    return result

if __name__ == "__main__":
#Test 1
    expected=24 # Result should be 4
    result= multiply_two_numbers(4,6)#testing for multiplying 2 numbers
    if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")
        
#Test 2
    expected=32 # Result should be 4
    result= multiply_two_numbers(-16,-2)#multiplying with negative numbers
    if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")


#Test 3
    expected=0 # Result should be 0
    result= multiply_two_numbers(16,0)#testing for an answer using a Zero Value
    if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
