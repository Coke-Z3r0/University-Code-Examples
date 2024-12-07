def greatest(a, b, c):
    biggest = a#Declaring the value in A to be the greatest, as it is the first value 
    if biggest < b: #checking if the value in B bigger than the current greatest value
        biggest = b
    else:
        biggest = biggest
    if biggest < c: #Checking if the value in C is bigger than the current greatest Value
        biggest = c
    else:
        biggest=biggest
    
    return biggest

if __name__ == "__main__":
#Test 1
   expected=12
   biggest = greatest(5,12,8)#testing with values so the value in the B position is the greatest
   if biggest == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {biggest}")
   else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {biggest}")

#Test 2
   expected=70
   biggest = greatest(70,12,34)#testing with values so the value in the A position is the greatest
   if biggest == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {biggest}")
   else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {biggest}")
        
#Test 3
   expected=43
   biggest = greatest(1,16,43)#testing with values so the value in the C position is the greatest
   if biggest == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {biggest}")
   else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {biggest}")
