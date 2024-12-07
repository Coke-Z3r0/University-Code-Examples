def multiply_subset(numbers, indices):
    result=1#initialising a results variable
    for index in indices:
        result *=numbers[index]#calculating the value of the result based on the index position of the Indices List
    
    return result

if __name__ == "__main__":
#Test 1
    expected=48 # Result should be 48
    result= multiply_subset([2,3,4,5,6,7,8], [0,2,4])#testing multiplying 3 numbers
    if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")


#Test 2
    expected=4 # Result should be 4
    result= multiply_subset([4,2,4,5,1], [2,4])#testing for multiplying 2 numbers
    if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")
        
#Test 3
    expected=378 # Result should be 378
    result= multiply_subset([4,3,6,7,1,78,4,9], [2,4,3,7])#testing for multiplying 4 numbers, out of  ascending order
    if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
