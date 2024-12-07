def adds(p1, p2):
    #This block of code ensures the 2 vectors added are of the same value 
    if len(p1) != len(p2):
    	result = 'None' 
    else:
	    result = [] #initialising the array for the result
	    for i in range (len(p1)):
	    	result.append(p1[i] + p2[i])#calculating the result based on the position in both arrays
    	
    return result 
    
if __name__ == "__main__":

# Test 1
   expected=[7,6,7]#testing with Normal Values
   result = adds([5,7,3],[2,-1,4])
   if result == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {result}")
   else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {result}")

#Test 2  
   expected='None' #testing for a None Result
   result = adds([5,7,3],[3,2])
   if result == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {result}")
   else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {result}")
        
#Test 3
   expected=[8,3,-2]
   result = adds([5,7,3],[3,-4,-5])#testing to see if it will produce a negative value in the result
   if result == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {result}")
   else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {result}")
