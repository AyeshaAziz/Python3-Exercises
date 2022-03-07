'''Exercise 1:
Create a dictionary that contains a list of people and one interesting fact about each of them. 
Display each person and their interesting fact to the screen. 
Next, change a fact about one of the people. 
Also add an additional person and corresponding fact. 
Display the new list of people and facts. 
Run the program multiple times and notice if the order changes.
'''
people = [
    {'name': 'Ali', 'fact': 'is a Doctor' },
    {'name': 'Ayesha', 'fact': 'is a Software Engineer' },
    {'name': 'Rehman', 'fact': 'loves cooking' }
]
def displayPeople():
    for person in people:
        print('\n' + person['name'] + ': ' + person['fact'])
        print()

displayPeople()
# change a fact about one of the people.
print('*' * 20)
print('\nChange List')
people[0]['fact'] = 'cannot drive'
newPerson = {'name': 'Ambreen', 'fact': 'is a teacher'}
people.append(newPerson)
displayPeople()



