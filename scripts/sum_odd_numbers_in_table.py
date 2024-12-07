def sum_odd_numbers_in_table(n):

    total_sum = 0 #Initialising the variable to store the sum of odd numbers
    
    for i in range (1,n+1):#iterating through the multiplication table
        for j in range (1, n+1):
            product = i*j 
            if product % 2 !=0: #checks if the product is odd
                total_sum+= product
                
    return total_sum

if __name__ == "__main__":
#Test 1
    expected=16 # Result should be 16
    total_sum= sum_odd_numbers_in_table(3)#
    if total_sum == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {total_sum}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {total_sum}")
        
#Test 2 
    expected=81 # Result should be 81
    total_sum= sum_odd_numbers_in_table(5)
    if total_sum == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {total_sum}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {total_sum}")
        
        
#Test 3
    expected=1 # Result should be 1
    total_sum= sum_odd_numbers_in_table(1)
    if total_sum == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {total_sum}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {total_sum}")
