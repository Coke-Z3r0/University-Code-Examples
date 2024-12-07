def sort_to_types(arbitrary_ordered_types):
# Separating the list into strings, integers, and floats
    strings = [item for item in arbitrary_ordered_types if isinstance(item, str)]
    integers = [item for item in arbitrary_ordered_types if isinstance(item, int)]
    floats = [item for item in arbitrary_ordered_types if isinstance(item, float)]
    
    ordered= strings + integers + floats#Combining the list again into its corrected order , starting with strings, integers, floats
    
    return ordered
if __name__ == "__main__":
# Test 1
    expected = ['banana', 'apple', 5, 42, 3.14, 2.71]#result should be an ordered list
    result =sort_to_types(['banana', 5, 3.14, 'apple', 42, 2.71])#stating the list to be used for this test
	                    
    if result == expected:
	    print(f"Test 1 Passed! Expected: {expected} Actual: {result}")
    else:
	    print(f"Test 1 Failed! Expected: {expected} Actual: {result}")
	    
# Test 2
    expected = ['orange', 'pear', 5, 13, 4.3, 2.92]#result should be the same as the input (testing with a preordered list
    result =sort_to_types(['orange', 'pear', 5, 13, 4.3, 2.92])#stating the list to be used for this test
	                    
    if result == expected:
	    print(f"Test 2 Passed! Expected: {expected} Actual: {result}")
    else:
	    print(f"Test 2 Failed! Expected: {expected} Actual: {result}")

# Test 3
    expected = ['peach', 5, 9.2]#result should be the same as the input (testing with a short list
    result =sort_to_types([5, 9.2, 'peach'])#stating the list to be used for this test
	                    
    if result == expected:
	    print(f"Test 3 Passed! Expected: {expected} Actual: {result}")
    else:
	    print(f"Test 3 Failed! Expected: {expected} Actual: {result}")
