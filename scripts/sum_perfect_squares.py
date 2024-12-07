def sum_perfect_squares(number):
    #variable to store the result of the perfect squares
    result = 0
    
    for i in range (1, number+1):
        result += i**2 #adding the square of I to the total sum
        
    return result

if __name__ == "__main__":    
#Test 1
    expected=30 # Result should be 30
    result= sum_perfect_squares(4)
    if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")
        
#Test 2
    expected=5 # Result should be 5
    result= sum_perfect_squares(2)
    if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")
        
#Test 3
    expected=91 # Result should be 91
    result= sum_perfect_squares(6)
    if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
