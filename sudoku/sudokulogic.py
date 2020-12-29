import pprint
import random
def if_valid(y,x,num):
    global list
    for i in range(0,9):
        if list[y][i]==num:
            return False
    for i in range(0,9):
        if list[i][x]==num:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if list[y0+i][x0+j]==num:
                return False
    return True

list = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

list[0][random.randint(0,8)] = 1
if list[0][8] != 1:
    list[random.randint(0,8)][8] = 9
    rand = 12
else:
    rand = 13
for int in range(rand):
    x = random.randint(0,8)
    y = random.randint(0,8)
    nums = random.randint(1,9)
    if if_valid(y,x,nums):
        list[y][x] = nums

def solver():
    global list
    for y in range(9):
        for x in range(9):
            if list[y][x] == 0:
                for num in range(1,10):
                    if if_valid(y,x,num):
                        list[y][x] = num
                        yield from solver()
                    else:
                        list[y][x] = 0
                return
    yield list

list_of_solutions = solver()
m = next(list_of_solutions)
for i in range(50):
    x = random.randint(0,8)
    y = random.randint(0,8)
    m[y][x] = 0
s = m
