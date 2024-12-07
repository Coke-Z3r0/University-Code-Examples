def weather_advice(sunny, rainy, windy, temperature):

    advice = []#Initialising the list for appending advice onto one-another
    
    if sunny: #Checking for sunny weather
        advice.append("Wear sun cream.")
        if temperature > 25: 
            advice.append("It's hot and sunny! Eat some ice cream.")
            
    if rainy: #Checking for rainy weather
        advice.append("Carry an umbrella.")
        if windy: #Checking if rainy and windy
            advice.append("It's windy! Hold onto your umbrella tightly.")
    
    if windy: #Checking for Windy Weather
        advice.append("Hold on to your hat.")
        
    return advice

if __name__ == "__main__":
#Test 1
    expected=['Wear sun cream.', "It's hot and sunny! Eat some ice cream."] # Testing for Hot and Sunny weather
    advice= (weather_advice(True, False, False, 30))
    if advice == expected:
        print(f"Test 1 passed! Expected: {expected}, Actual: {advice}")
    else:
        print(f"Test 1 failed! Expected: {expected}, Actual: {advice}")
        

#Test 2
    expected=['Carry an umbrella.', "It's windy! Hold onto your umbrella tightly.", 'Hold on to your hat.']
 # Testing for Rainy and Windy Weather
    advice= (weather_advice(False, True, True, 10))
    if advice == expected:
        print(f"Test 2 passed! Expected: {expected}, Actual: {advice}")
    else:
        print(f"Test 2 failed! Expected: {expected}, Actual: {advice}")
        
#Test 3
    expected=['Wear sun cream.', 'Hold on to your hat.']
 # Testing for Sunny and Windy Weather
    advice= (weather_advice(True, False, True, 20))
    if advice == expected:
        print(f"Test 3 passed! Expected: {expected}, Actual: {advice}")
    else:
        print(f"Test 3 failed! Expected: {expected}, Actual: {advice}")
        
#Test 4
    expected=['Carry an umbrella.']
 # Testing for Rainy Weather
    advice= (weather_advice(False, True, False, 18))
    if advice == expected:
        print(f"Test 4 passed! Expected: {expected}, Actual: {advice}")
    else:
        print(f"Test 4 failed! Expected: {expected}, Actual: {advice}")
