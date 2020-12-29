#tests the board if it is valid or not
from graphics import *
from graphicboardforsudoku import *
import pprint
win = GraphWin("Sudoku" ,width = 540, height = 540)
for i in lines():
    i.draw(win)
row = [0]
col = [0]
x = 1
count = 0
for i in range (1,10):
    row.append(60*x)
    col.append(60*x)
    x +=1

def inside(point, rectangle):
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right
    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

while True:
    clickpoint = win.checkMouse()
    y = 0
    if clickpoint != None:
        for ii in range(1,10):
            x = 0
            for jj in range(1,10):
                if inside(clickpoint,Rectangle(Point(col[x],row[y]),Point(col[x+1],row[y+1]))):
                    pp = Circle(Point(col[x+1]-30,row[y+1]-30),7)
                    pp.draw(win)
                    break
                x += 1
            y+=1


win.close()




input = game.playing(x)
if input  == 3:
    window.close()
elif input == 2:
    window.close()
    game.main_menu_window()
elif input == 1:
    print("ha")
