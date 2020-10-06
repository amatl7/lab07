
# Activity 1
strings = input("Enter the strings! ").split()
for i in range(len(strings)):
    string_holder = strings[i]
    if string_holder[-1:] == string_holder[:1]:
        if len(string_holder) >= 2:
            print(string_holder)

# Activity 2
listylist = input("Enter numbers! ").split()
for i in range(len(listylist)):
    listylist[i] = int(listylist[i])
user_value = int(input("Enter the value! "))
for i in range(len(listylist)):
    if listylist[i] < user_value:
        print(listylist[i], " ", end="")

# Activity 3
#getting sentence and letter to be checked
sentence = input('Enter a sentence: ')
checkLet = input('What letter do you want to check? ')
num_count = 0
#looping over string in order to determine the amount of times the letter was used

for i in sentence:
    if checkLet == i:
        num_count += 1
#print the amount of times it was used
print(checkLet, 'was used', num_count, 'times')

#function solver
from math import *
min = float(input('Enter minimum value: '))
max = float(input('Enter maximum value: '))
current_val = min
list_values = []
#getting the increments that will be plugged into y(x)
increments = (max-min) / 100
for i in range(101):
    current_val += min
    x = current_val
    y = sin(x) / (sin(x/10) + x/10)
    list_values.append(y)

print(list_values)
