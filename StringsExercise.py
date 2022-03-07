
# Ex÷ercise 1:
# Write a Python program that uses three variables. 
# The variables in your program will be animal, vegetable, and mineral. 
# Assign a string value to each one of the variables. 
# Your program should display "Here is an animal, a vegetable, and a mineral." 
# Next, display the value for animal, followed by vegetable, and finally mineral. 
# Each one of the values should be printed on their own line. 
# Your program will display four lines in total.

def exerciseOne():
    print('Exercise One')
    animal = 'cat'
    vegetable = 'broccolli'
    mineral = 'gold'
    line = 'Here is an animal, a vegetable, and a mineral.'

    print(line + '\n' + animal + '\n' + vegetable + '\n' + mineral + '\n')
# exerciseOne()

# Exercise 2:
# Write a Python program that prompts the user for input and 
# simply repeats what the user entered.

def excerciseTwo():
    print('Exercise Two')
    userInput = input('Please type something and press enter: ')
    print('You entered:\n' + userInput)

# Exercise 3:
# Write a Python program that prompts for input and 
# displays a cat "saying" what was provided by the user. 
# Place the input provided by the user inside a speech bubble. 
# Make the speech bubble expand or contract to fit around the input provided by the user.

def catSay(text):
    length = len(text)

    print('           {}'.format('_' * length))
    print('         < {} >'.format(text))
    print('           {}'.format('-' * length))
    print('         /')
    print('  /\_/\ /')
    print(' ( o.o )')
    print('  > ^ <')

def main():
    text = input('What would you like the cat to say? ') 
    catSay(text)

if __name__ == '__main__': main()
