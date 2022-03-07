

print('1. Hello Word')
print('Hello ' * 5)

print('\n2. Formatting Strings')
print('I {0} {1} {2}'.format('am', 'learnning', 'Python'))
print('I {0} {1}. {1} {0}s me. '.format('love', 'Python'))
print('I {0} {1} version {2}'.format('love', 'Python', 3))
version_no = 3
print('I {0} {1} version {2}'.format('love', 'Python', version_no))
print('-----------------------------')

#{0 : 5} => 1st value provided in the formar and make it atleast 8 characters wide
#{1 : 8} => 2nd value provided in the formar and make it atleast 5 characters wide  
print('{0:8} | {1:5}'.format('Fruit','Quantity')) 
print('{0:8} | {1:5}'.format('Apple',3)) 
print('{0:8} | {1:5}'.format('Oranges',10)) 

print('\n3. Formatting String Alignment')
# < Left, > Right, ^ Center, .nf (.2f) 2decimal places 
print('{0:8} | {1:<8}'.format('Fruit','Quantity')) 
print('{0:8} | {1:<8}'.format('Banana',13)) 
print('{0:8} | {1:>8}'.format('Apple',3)) 
print('{0:8} | {1:^8.2f}'.format('Oranges',10)) 
print('{0:8} | {1:^8.2f}'.format('Oranges',10.7763)) 

print('-----------------------------')
print('-----------------------------')

print('\n4. Getting user input from key board')
inputString = input('Enter a number please: ')
no = None
try:
    no = int(inputString) 
except ValueError:
    print('Invalid number')

if(type(no) == int):
    print('you have entered: {}'.format(no))
 
