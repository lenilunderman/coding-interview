# functions
def countNumbers(num):
    for i in range(0, num +1):
        print(i)
    # return the result
    return i
countNumbers(10)

def sales(item, price, day):
    return(f'I bought {item} and it cost me {price}, it was great a week {day}')

sales('uvas',23, 'saturday')