def divide_two_numbers(m, n): 
    if m==0 or n==0:
    	result = "NAN"#Returning NAN If any digit is Zero, as you cannot divide by Zero
    else:
    	result = (m/n)#Dividing the first digit by the second digit
    
    return result

if __name__ == "__main__":
# Test 1
   expected=5#Testing for a Normal Result
   result = divide_two_numbers(10,2)
   if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
   else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")
        
        
# Test 2
   expected='NAN'#Testing with a NAN result on the Second Value
   result = divide_two_numbers(5,0)
   if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
   else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")
        
        
# Test 3
   expected='NAN'#Testing for a NAN result on the First Value
   result = divide_two_numbers(0,20)
   if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
   else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
