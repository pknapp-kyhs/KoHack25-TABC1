pos = -1
def search(list, num):
    i = 0

    while 1 < len(list):
        if list[i] == num:
            globals() ['pos'] = i
            return True
        i = i +1
    return False
two = 2
three = 3
four = 4
list = [2, 3, 4]
print(list)
num = int(input('pick one from the list: '))
if search(list, num):
    print('yay')
else:
    print('Not found')