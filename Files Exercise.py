'''Exercise 1:
Practice Exercises ­ Files
Create a program that opens file.txt. 
Read each line of the file and prepend it with a line number.'''
        
# with open('file.txt', 'w+') as file:
#     file.write('This file has been created by phthon.\n')
#     file.write('This file will be used to learn about files in python.\n')

# status = 'closed' if file.closed else 'not closed'
# print('File is {} automatically'.format(status))

# # append
# with open('file.txt', 'a+') as file:

#     print('current position: ', file.tell())
#     # move cursor to the beginning of the file
#     position = file.seek(0)
#     print('current position: ', file.tell())
#     file.write('1. ')
#     # print(file.read())

with open('file.txt') as file: 
    line_number = 1
    for line in file:
        print('{}: {}'.format(line_number, line.rstrip())) 
        line_number += 1
