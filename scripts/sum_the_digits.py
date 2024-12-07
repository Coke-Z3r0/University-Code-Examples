def sum_the_digits(number):
    # Converting the numbers to a string and summing the digits
    result = sum(int(digit) for digit in str(number))
    
    return result
    
if __name__ == "__main__":
#Test 1
    expected=10 # Result should be 10
    result= sum_the_digits(1234)#testing with a monotonically increasing number
    if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")
        
#Test 2
    expected=22 # Result should be 30
    result= sum_the_digits(9643) #testing with a monotonically decreasing number
    if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")
        
#Test 3
    expected=24 # Result should be 22
    result= sum_the_digits(17394) #testing with a non monotonic number
    if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
