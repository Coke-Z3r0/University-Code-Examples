def is_even_and_positive(number):
    if number % 2 ==0 and number>=0: #when a number is divided by 2 and leaves a remainder, it is odd, and if the number is less than 0, it is negative
        result=True
    else:
        result=False
    return result

if __name__ == "__main__":
#Test 1
    expected=True
    result = is_even_and_positive(12)#testing with an even number
    if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")

#Test 2
    expected=False
    result = is_even_and_positive(9)#testing with an odd number
    if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")
        
#Test 3
    expected=False
    result = is_even_and_positive(-6)#testing with a negative even number
    if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
