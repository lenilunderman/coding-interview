primes = [2, 3, 5, 7, 11]
print(primes)

# list method to append ()
orders = ['daisies', 'periwinkle']
orders.append('roses')
print(orders)

#list indexes list[index]
orders[2]
print(orders[2])

#count() search an list and count how many of that instances are inside 
backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')
print(numPen)

# sorted() function is better than sort() method, because it create a new list from that.
unsortedList = [4, 2, 1, 3]
sorted_list = sorted(unsortedList)

# return a unique list with no duplicates
old_list = [2,4,6,8,10,8,3,2] 
uniquelist = list(set(old_list))
print(uniquelist)

# adding lists together.
cakes = ['chocolate','avela','goiaba']
sweets = ['brigadeiro', 'doce de morango']
party_list = cakes + sweets 