#Sudoku open source program for CAS
from graphics import *
from graphicboardforsudoku import *
import random

list = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

listktkt = [[]]

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

def if_valid_final(y,x,num):
    global listktkt
    for i in range(0,9):
        if listktkt[y][i]==num:
            return False
    for i in range(0,9):
        if listktkt[i][x]==num:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if listktkt[y0+i][x0+j]==num:
                return False
    return True

def makingboard():
    global list
    global listktkt
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
    listktkt = list
    list = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

def solver():
    global listktkt
    for y in range(9):
        for x in range(9):
            if listktkt[y][x] == 0:
                for num in range(1,10):
                    if if_valid_final(y,x,num):
                        listktkt[y][x] = num
                        yield from solver()
                    else:
                        listktkt[y][x] = 0
                return
    yield listktkt

def mala():
    makingboard()
    list_of_solutions = solver()
    m = next(list_of_solutions)
    for i in range(50):
        x = random.randint(0,8)
        y = random.randint(0,8)
        m[y][x] = 0
    return m

def initial_window(x):
    window = GraphWin("Sudoku" ,width = 540, height = 540) ## WARNING: width  = 600
    winn = GraphWin("Sudoku" ,width = 300, height = 270)
    winnie = GraphWin("Numbers" ,width = 360, height = 150)
    if x == 1:
        background = color_rgb(0,128,128)
        liness = color_rgb(225,174,1)
        z = color_rgb(225,174,1)
    elif x == 2:
        background = color_rgb(0,0,0)
        liness = color_rgb(224,255,255)
        z = color_rgb(224,255,255)
    elif x == 3:
        background = color_rgb(0,0,0)
        liness = color_rgb(192,192,192)
        z = color_rgb(192,192,192)
    elif x == 4:
        background = color_rgb(0,0,0)
        liness = color_rgb(255,7,58)
        z = color_rgb(255,7,58)
    elif x == 5:
        background = color_rgb(0,128,128)
        liness = color_rgb(135,206,250)
        z = color_rgb(135,206,250)
    window.setBackground(background)
    winn.setBackground(z)
    winnie.setBackground(z)
    for i in lines():
        i.setFill(liness)
        i.draw(window)
    check = Rectangle(Point(50, 10), Point(250, 80))
    check.setWidth(5)
    check.setOutline(background)
    txt1 = Text(Point(150,45),"Check Board")
    txt1.setSize(20)
    txt1.setTextColor(background)
    play_again = Rectangle(Point(50, 100), Point(250, 170))
    play_again.setWidth(5)
    play_again.setOutline(background)
    txt2 =Text(Point(150,135),"Play Again")
    txt2.setSize(20)
    txt2.setTextColor(background)
    quit = Rectangle(Point(50, 190), Point(250, 260))
    quit.setWidth(5)
    quit.setOutline(background)
    txt3 =Text(Point(150,225),"Quit")
    txt3.setSize(20)
    txt3.setTextColor(background)
    check.draw(winn)
    play_again.draw(winn)
    quit.draw(winn)
    txt1.draw(winn)
    txt2.draw(winn)
    txt3.draw(winn)

    board = mala()
    yy = 30
    for i in board:
        xx = 30
        for p in i:
            if p == 0:
                pass
            else:
                txt = Text(Point(xx,yy),p)
                txt.setTextColor(z)
                txt.setSize(25)
                txt.draw(window)
            xx += 60
        yy += 60

    numtxts1 = Text(Point(20,45),"1")
    numtxts2 = Text(Point(60,45),"2")
    numtxts3 = Text(Point(100,45),"3")
    numtxts4 = Text(Point(140,45),"4")
    numtxts5 = Text(Point(180,45),"5")
    numtxts6 = Text(Point(220,45),"6")
    numtxts7 = Text(Point(260,45),"7")
    numtxts8 = Text(Point(300,45),"8")
    numtxts9 = Text(Point(340,45),"9")
    clearb = Text(Point(70,115),"Clear space")
    clearb.setTextColor(background)
    clearb.setSize(15)
    clearb.draw(winnie)
    tepeot = Rectangle(Point(5,90),Point(130,145))
    tepeot.setWidth(3)
    tepeot.setOutline(background)
    tepeot.draw(winnie)
    pencil = Text(Point(280,115),"Pencil mark")
    pencil.setTextColor(background)
    pencil.setSize(15)
    pencil.draw(winnie)
    ppppppp = Rectangle(Point(215,90),Point(340,145))
    ppppppp.setWidth(3)
    ppppppp.setOutline(background)
    ppppppp.draw(winnie)
    topx = 5
    col1 = [5]
    bottomx = 35
    col2 = [35]
    kras = [numtxts1,numtxts2,numtxts3,numtxts4,numtxts5,numtxts6,numtxts7,numtxts8,numtxts9]
    for ix in range(0,9):
        rectt = Rectangle(Point(topx,20),Point(bottomx,70))
        todraw = kras[ix]
        todraw.setSize(30)
        todraw.setTextColor(background)
        todraw.draw(winnie)
        rectt.setOutline(background)
        rectt.draw(winnie)
        topx += 40
        col1.append(topx)
        bottomx += 40
        col2.append(bottomx)

    while True:
        clickpoint = window.checkMouse()
        clickity = winn.checkMouse()
        clip = winnie.checkMouse()
        if clip != None:
            xifx = 0
            for jjj in range(1,10):
                xgames = 25
                if inside(clip,Rectangle(Point(col1[xifx],20),Point(col2[xifx],70))):
                    num = xifx + 1
                    break
                xifx += 1
                if inside(clip,Rectangle(Point(5,90),Point(130,145))):
                    num = 0
                if inside(clip,Rectangle(Point(215,90),Point(340,145))):
                    xgames = 20
        if clickpoint != None:
            y = 0
            row = [0]
            col = [0]
            x = 1
            count = 0
            for i in range (1,10):
                row.append(60*x)
                col.append(60*x)
                x +=1
            for ii in range(1,10):
                x = 0
                for jj in range(1,10):
                    if inside(clickpoint,Rectangle(Point(col[x],row[y]),Point(col[x+1],row[y+1]))):
                        cover = Circle(Point(col[x+1]-30,row[y+1]-30),15)
                        cover.setFill(background)
                        cover.setOutline(background)
                        cover.draw(window)
                        if num != 0:
                            tct = Text(Point(col[x+1]-30,row[y+1]-30),str(num))
                            tct.setTextColor(color_rgb(0,255,0))
                            tct.setSize(xgames)
                            tct.draw(window)
                        board[y][x] = num
                    x += 1
                y+=1
        x += 1
        if clickity != None:
            if inside(clickity,Rectangle(Point(50, 10), Point(250, 80))):
                endofg = 1
                for i in range(0,9):
                    for y in range(0,9):
                        if board[i][y]==0:
                            endofg = 0
                for i in range(9):
                    row = {}
                    column = {}
                    block = {}
                    row_cube = 3 * (i//3)
                    column_cube = 3 * (i%3)
                    for j in range(9):
                        if board[i][j]!= 0 and board[i][j] in row:
                            endofg = 0
                        row[board[i][j]] = 1
                        if board[j][i]!= 0 and board[j][i] in column:
                            endofg = 0
                        column[board[j][i]] = 1
                        rc= row_cube+j//3
                        cc = column_cube + j%3
                        if board[rc][cc] in block and board[rc][cc]!= 0:
                            endofg = 0
                        block[board[rc][cc]]=1

                cov = Circle(Point(280,45),10)
                if endofg == 0:
                    cov.setFill("blue")
                    cov.setOutline("blue")
                    cov.draw(winn)
                elif endofg == 1:
                    cov.setFill("green")
                    cov.setOutline("green")
                    cov.draw(winn)
            elif inside(clickity,Rectangle(Point(50, 100), Point(250, 170))):
                winn.close()
                window.close()
                winnie.close()
                main_menu_window()
                break
            elif inside(clickity,Rectangle(Point(50, 190), Point(250, 260))):
                window.close()
                winn.close()
                winnie.close()
                break
            clickpoint = window.checkMouse()

def main_menu_window():
    win = GraphWin("Sudoku" ,width = 930, height = 600)
    win.setBackground(color_rgb(0,0,0))
    img = Image(Point(450,300), "sudokuboardpic.png")
    img.draw(win)
    heading = Text(Point(220,60), "Sudoku Game")
    heading.setTextColor(color_rgb(0,255,0))
    heading.setSize(30)
    heading.setFace("times roman")
    heading.setStyle("bold italic")
    heading.draw(win)
    text = Text(Point(220,250), """
    Sudoku is a puzzle game designed for
    a single player, much like a crossword
    puzzle. The puzzle itself is nothing more
    than a grid of little boxes called “cells”.
    They are stacked nine high and nine wide,
    making 81 cells total. The puzzle comes
    with some of the cells filled in.
    Rules for this game can be found online.

    Click on the corresponding buttons to
    select a board theme pellete and start
    the game. When finished, check board. If
    blue dot: something went wrong, if green
    dot: good job! It's right.""")
    text.setTextColor(color_rgb(0,255,0))
    text.setSize(15)
    text.setFace("times roman")
    text.setStyle("bold italic")
    text.draw(win)
    sign = Text(Point(850,570),"Made by: Tushit Jain")
    sign.setTextColor(color_rgb(0,255,0))
    sign.setSize(10)
    sign.setFace("times roman")
    sign.setStyle("bold italic")
    sign.draw(win)
    for ii in buttons():
        ii.draw(win)
    x = 1
    aCircle = Circle(Point(60,500),10)
    while True:
        clickpoint = win.getMouse()
        aCircle.undraw()
        if inside(clickpoint,Rectangle(Point(40, 450), Point(120, 480))):
            x = 1
            aCircle = Circle(Point(80,500),10)
            aCircle.setFill(color_rgb(0,255,0))
            aCircle.draw(win)
        elif inside(clickpoint,Rectangle(Point(140, 450), Point(220, 480))):
            x = 2
            aCircle = Circle(Point(180,500),10)
            aCircle.setFill(color_rgb(0,255,0))
            aCircle.draw(win)
        elif inside(clickpoint,Rectangle(Point(240, 450), Point(320, 480))):
            x = 3
            aCircle = Circle(Point(280,500),10)
            aCircle.setFill(color_rgb(0,255,0))
            aCircle.draw(win)
        elif inside(clickpoint,Rectangle(Point(340, 450), Point(420, 480))):
            x = 4
            aCircle = Circle(Point(380,500),10)
            aCircle.setFill(color_rgb(0,255,0))
            aCircle.draw(win)
        elif inside(clickpoint,Rectangle(Point(440, 450), Point(520, 480))):
            x = 5
            aCircle = Circle(Point(480,500),10)
            aCircle.setFill(color_rgb(0,255,0))
            aCircle.draw(win)
        elif inside(clickpoint,Rectangle(Point(180, 520), Point(300, 550))):
            break
    win.close()
    initial_window(x)

def buttons():
    list =[]
    start = Rectangle(Point(180, 520), Point(300, 550))
    start.setFill(color_rgb(0,0,0))
    O1c1 = Rectangle(Point(40, 450), Point(120, 480))
    O1c1.setFill(color_rgb(0,128,128))
    O1c2 = Rectangle(Point(45, 455), Point(115, 475))
    O1c2.setFill(color_rgb(225,174,1))
    ############################################################################
    O2c1 = Rectangle(Point(140, 450), Point(220, 480))
    O2c1.setFill(color_rgb(0,0,0))
    O2c2 = Rectangle(Point(145, 455), Point(215, 475))
    O2c2.setFill(color_rgb(224,255,255))
    ############################################################################
    O3c1 = Rectangle(Point(240, 450), Point(320, 480))
    O3c1.setFill(color_rgb(0,0,0))
    O3c2 = Rectangle(Point(245, 455), Point(315, 475))
    O3c2.setFill(color_rgb(192,192,192))
    ############################################################################
    O4c1 = Rectangle(Point(340, 450), Point(420, 480))
    O4c1.setFill(color_rgb(0,0,0))
    O4c2 = Rectangle(Point(345, 455), Point(415, 475))
    O4c2.setFill(color_rgb(255,7,58))
    ############################################################################
    O5c1 = Rectangle(Point(440, 450), Point(520, 480))
    O5c1.setFill(color_rgb(211,211,211))
    O5c2 = Rectangle(Point(445, 455), Point(515, 475))
    O5c2.setFill(color_rgb(135,206,250))
    ##############################################################################
    txtxt = Text(Point(240,535),"Start")
    txtxt.setTextColor(color_rgb(100,255,100))
    txtxt.setSize(20)
    txtxt.setFace("times roman")
    txtxt.setStyle("bold italic")
    list.append(start)
    list.append(O1c1)
    list.append(O1c2)
    list.append(O2c1)
    list.append(O2c2)
    list.append(O3c1)
    list.append(O3c2)
    list.append(O4c1)
    list.append(O4c2)
    list.append(O5c1)
    list.append(O5c2)
    list.append(txtxt)
    return list

def inside(point, rectangle):
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right
    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

main_menu_window()
