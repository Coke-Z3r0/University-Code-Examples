def area_of_circle(radius):

    PI = 3.142 #Declaring the predefined value of PI 
    area = PI*(radius**2)#calculating the area, based on the radius provided and using the formula pi*r^2
    
    return area

if __name__ == "__main__":
# Test 1
	expected = 153.958 #result should be 153.958
	radius = 7 #initialising the radius variable for this test
	area =area_of_circle(radius) #calling the area_of_circle function
	if area == expected:
		print(f"Test 1 Passed! Expected: {expected} Actual: {area}")
	else:
		print(f"Test 1 Failed! Expected: {expected} Actual: {area}")


# Test 2
	expected = 0 #result should be 0
	radius = 0 #initialising the radius variable for this test, using a normal value
	area =area_of_circle(radius) #calling the area_of_circle function
	if area == expected:
		print(f"Test 2 Passed! Expected: {expected} Actual: {area}")
	else:
		print(f"Test 2 Failed! Expected: {expected} Actual: {area}")

# Test 3
	expected = 12.568 #result should be 12.568
	radius = -2 #initialising the radius variable for this test, using a negative value
	area =area_of_circle(radius) #calling the area_of_circle function
	if area == expected:
		print(f"Test 1 Passed! Expected: {expected} Actual: {area}")
	else:
		print(f"Test 1 Failed! Expected: {expected} Actual: {area}")
