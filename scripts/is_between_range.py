def is_between_range(number, range):
    between=range[0] <=number<=range[1]# Checks if the number is included or between the range
    return between

if __name__ == "__main__":
#Test 1
   expected=True #Testing for a True Value
   between = (is_between_range(5,[1,10]))#Value should return True
   if between == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {between}")
   else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {between}")
        
#Test 2
   expected=False #Testing for a False Value
   between = (is_between_range(12,[1,10]))#Value should return False
   if between == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {between}")
   else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {between}")
        
#Test 3
   expected=True #Testing for a True Value using a below Zero Value
   between = (is_between_range(-2,[-5,0]))#Value should return True
   if between == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {between}")
   else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {between}")
