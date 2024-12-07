def numeric_from_strings(list_of_strings):

    word_to_digit = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 
        'four': '4', 'five': '5', 'six': '6', 'seven': '7', 
        'eight': '8', 'nine': '9'#Declaring the list of words comparing it to its corresponding digit
    } 
    number_str = ''.join(word_to_digit[word] for word in list_of_strings)# Converting each word in the list to its corresponding digit and joining them into a single string
    
    result =int(number_str)
    return result
    
if __name__ == "__main__":
# Test 1
    expected = 10290 #result should be 10290
    list_of_strings=['one','zero','two','nine','zero']#stating the numbers for this test in string form
	                    
    result = numeric_from_strings(list_of_strings) #calling the numeric_from_string function
    if result == expected:
	    print(f"Test 1 Passed! Expected: {expected} Actual: {result}")
    else:
	    print(f"Test 1 Failed! Expected: {expected} Actual: {result}")
	    
# Test 2
    expected = 45928 #result should be 45928 
    list_of_strings=['four','five','nine','two','eight']#stating the numbers for this test in string form
	                    
    result = numeric_from_strings(list_of_strings) #calling the numeric_from_string function
    if result == expected:
	    print(f"Test 2 Passed! Expected: {expected} Actual: {result}")
    else:
	    print(f"Test 2 Failed! Expected: {expected} Actual: {result}")
	    
# Test 3
    expected = 42 #result should be 42
    list_of_strings=['four','two']#stating the numbers for this test in string form
	                    
    result = numeric_from_strings(list_of_strings) #calling the numeric_from_string function
    if result == expected:
	    print(f"Test 3 Passed! Expected: {expected} Actual: {result}")
    else:
	    print(f"Test 3 Failed! Expected: {expected} Actual: {result}")
