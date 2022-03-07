'''Exercise 1:
Practice Exercises ­ Lists
Create a Python program that captures and displays a person's to­do list. 
Continually prompt the user for another item until they enter a blank item. 
After all the items are entered, display the to­do list back to the user.'''

from csv import list_dialects
from typing import Tuple


def createtoDoList():
    toDoList = []
    done = False
    while not done:
        toDoItem = input('Enterataskforyourto­dolist. Press <enter> whendone: ') 
        if len(toDoItem) != 0:
            toDoList.append(toDoItem)
            print('Task added to the list')
        else:
            done = True
    return toDoList

def displayToDoList():
    list = createtoDoList()
    print('To Do List')
    print('-' *15)
    for item in list:
        print(item)
    print('-' *15)
    

# displayToDoList()

print('-' * 20)
tuple = ('a','b','c')
print('tuple', tuple)
# Tuple to list
print('\nType of tuple before is:  {}'.format(type(tuple)))
tupleToList = list(tuple)
print('\nType of tuple after is:  {}'.format(type(tupleToList)))

newList = [1,2,3,4,5]
print('\nlist', newList)
newList.append(6)
print('updated list', newList)

# List to Tuple
print('\nType of list before is:  {}'.format(type(newList)))
listToTuple = tuple(newList)
print('\nType of list after is:  {}'.format(type(listToTuple)))


