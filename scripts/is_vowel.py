def is_vowel(character):
    vowel = "AaEeIiOoUu"#Stating the vowels to search for, in upper and lower case
    
    if character in vowel:#checking the list of vowels to see if the given letter is in the list
        valid=True
    else:
        valid=False
    
    return valid

if __name__ == "__main__":
#Test 1
    expected=True # Result should be true(Vowel in Upper Case)
    valid= is_vowel('A')
    if valid == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {valid}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {valid}")
        
#Test 2
    expected=False # Result should be False(non Vowel Character)
    valid= is_vowel('h')
    if valid == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {valid}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {valid}")

#Test 3
    expected=True # Result should be true(Vowel in Lower Case)
    valid= is_vowel('u')
    if valid == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {valid}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {valid}")
