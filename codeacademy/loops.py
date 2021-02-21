# The important use of break
numbers = [0, 254, 2, -1, 3]
for i in numbers:
    if i < 0:
        print('Negative number detected', i)
        break
    print('the number is: ', i)


# While loops running one time
hungry = True
while hungry:
    print('Time to ear')
    hungry = False

# loop to run 3 times
counter = 1
while counter <= 3:
    print(counter)
    counter +=1

# nested loops
groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

for group in groups:
    for name in group:
        print(name)