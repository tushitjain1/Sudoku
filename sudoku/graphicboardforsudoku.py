#test for sudoku
from graphics import *
def lines():
    all_lines =[]
    total = 540
    bap = 0
    for x in range(2):
        temps = grid_lines((total/3)+bap,total*0,(total/3)+bap,total)
        temps.setWidth(5)
        all_lines.append(temps) # vertical main
        temps2 = grid_lines(total*0,(total/3)+bap,total,(total/3)+bap)
        temps2.setWidth(5)
        all_lines.append(temps2) # horizontal main
        bap += 180

    random = 540/9
    for y in range(9):
        all_lines.append(grid_lines(random,total*0,random,total)) #vertical lines
        all_lines.append(grid_lines(total*0,random,total,random)) #horizontal lines
        random += (540/9)
    return all_lines

def grid_lines(x1,y1,x2,y2):
    return Line(Point(x1,y1), Point(x2,y2))
