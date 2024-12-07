def calculate_percentage(part, total):
    if part ==0 or total==0:
    	percent= 'Undefined'#Preventing against a value being 0, as this would result in an error
    else:
    	percent=(part/total)*100 #calculating the percentage by using Numerator over Denominator and multiplying the value by 100
    
    return percent

if __name__ == "__main__":
#Test 1
   expected=20
   percent = calculate_percentage(30,150)#testing with Normal Values
   if percent == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {percent}")
   else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {percent}")

#Test 2
   expected='Undefined'
   percent = calculate_percentage(30,0)#Testing with a Zero Value
   if percent == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {percent}")
   else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {percent}")

#Test 3
   expected=46.7 #Testing for a float Value as the percentage result
   percent = calculate_percentage(70,150)# Using numbers that should produce a float
   if percent == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {percent}")
   else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {percent}")
