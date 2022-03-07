'''Exercise 1:
Let's assume you are planning to use your Python skills to build a social networking service. You decide to host your application on servers running in the cloud. You pick a hosting provider that charges $0.51 per hour. You will launch your service using one server and want to know how much it will cost to operate per day and per month.
Write a Python program that displays the answers to the following questions: How much does it cost to operate one server per day?
How much does it cost to operate one server per month?'''
hourlyChargesOneServer = 0.51
hoursInADay = 12
monthDays = 30

dailyCost = hoursInADay * hourlyChargesOneServer
monthlyCost = dailyCost * monthDays

print('\nHosting cost to operate one server per day: $' + str(dailyCost))
print('\nHosting cost to operate one server per month: ${0:.2f}'.format(monthlyCost))

'''
Exercise 2:
Building on the previous example, let's also assume that you have saved $918 to fund your new adventure. You wonder how many days you can keep one server running before your money runs out. Of course, you hope your social network becomes popular and requires 20 servers to keep up with the demand. How much will it cost to operate at that point?
Write a Python program that displays the answers to the following questions: How much does it cost to operate one server per day?
How much does it cost to operate one server per month?
How much does it cost to operate twenty servers per day?
How much does it cost to operate twenty servers per month? How many days can I operate one server with $918?'''

savings = 918
twentyServersPerDay = dailyCost * 20
twentyServersPerMonth = twentyServersPerDay * monthDays


print('\nCost to operate twenty servers per day: ${0:.2f}'.format(twentyServersPerDay))
print('\nCost to operate twenty servers per month: ${0:.2f}'.format(twentyServersPerMonth))
print('\nHow many days can I operate one server with savings: ' + str(int(twentyServersPerMonth/savings)))
print('\n')