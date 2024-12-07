def is_above_threshold(number, threshold):
    # function for checking if the given number is above the threshold number
    if number < threshold:
        above=0
    else:
        above=1
    return above

if __name__ == "__main__":
#Test 1
    expected=1
    above = is_above_threshold(15,10)#testing with a number greater than the threshold
    if above == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {above}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {above}")
        
#Test 2
    expected=0
    above = is_above_threshold(4,10)#testing with a number less than the threshold
    if above == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {above}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {above}")
        
#Test 3
    expected=1
    above = is_above_threshold(15,15)#testing with Values equal to each other
    if above == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {above}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {above}")
