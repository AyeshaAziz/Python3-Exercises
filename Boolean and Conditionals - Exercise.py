'''Exercise 1:
Create a program that asks the user how far they want to travel. 
If they want to travel less than three miles tell them to walk. 
If they want to travel more than three miles, 
but less than three hundred miles, tell them to drive. 
If they want to travel three hundred miles or more tell them to fly.
'''
miles = int(input('Please enter miles that you want to travel?: '))
minMiles = 3
maxMiles = 300

if miles <= minMiles:
    print('Please walk')
elif miles > minMiles and miles < maxMiles:
    print('Please drive')
elif miles >= maxMiles:
    print('Please fly')
