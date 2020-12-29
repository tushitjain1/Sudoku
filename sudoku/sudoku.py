#Sudoku open source program for CAS
from graphics import *
from graphicboardforsudoku import *
from sudokulogic import s
class game:
    def __init__ (self,initial_window,main_menu_window,buttons,inside):
        self.initial_window = initial_window
        self.main_menu_window = main_menu_window
        self.buttons = buttons
        self.inside = inside


    def initial_window(x):
        window = GraphWin("Sudoku" ,width = 540, height = 540) ## WARNING: width  = 600
        winn = GraphWin("Sudoku" ,width = 300, height = 270)
        board = s
        if x == 1:
            backgound = color_rgb(0,128,128)
            liness = color_rgb(225,174,1)
            z = color_rgb(225,174,1)
            winn.setBackground(color_rgb(225,174,1))
            other = color_rgb(0,128,128)
        elif x == 2:
            backgound = color_rgb(0,0,0)
            liness = color_rgb(224,255,255)
            z = color_rgb(224,255,255)
            winn.setBackground(color_rgb(224,255,255))
            other = color_rgb(0,0,0)
        elif x == 3:
            backgound = color_rgb(0,0,0)
            liness = color_rgb(192,192,192)
            z = color_rgb(192,192,192)
            winn.setBackground(color_rgb(192,192,192))
            other = color_rgb(0,0,0)
        elif x == 4:
            backgound = color_rgb(0,0,0)
            liness = color_rgb(255,7,58)
            z = color_rgb(255,7,58)
            winn.setBackground(color_rgb(255,7,58))
            other = color_rgb(0,0,0)
        elif x == 5:
            backgound = color_rgb(0,128,128)
            liness = color_rgb(135,206,250)
            z = color_rgb(135,206,250)
            winn.setBackground(color_rgb(135,206,250))
        window.setBackground(backgound)
        for i in lines():
            i.setFill(liness)
            i.draw(window)
        check = Rectangle(Point(50, 10), Point(250, 80))
        check.setWidth(5)
        check.setOutline(other)
        txt1 = Text(Point(150,45),"Check Baord")
        txt1.setSize(20)
        txt1.setTextColor(other)
        play_again = Rectangle(Point(50, 100), Point(250, 170))
        play_again.setWidth(5)
        play_again.setOutline(other)
        txt2 =Text(Point(150,135),"Play Again")
        txt2.setSize(20)
        txt2.setTextColor(other)
        quit = Rectangle(Point(50, 190), Point(250, 260))
        quit.setWidth(5)
        quit.setOutline(other)
        txt3 =Text(Point(150,225),"Quit")
        txt3.setSize(20)
        txt3.setTextColor(other)
        check.draw(winn)
        play_again.draw(winn)
        quit.draw(winn)
        txt1.draw(winn)
        txt2.draw(winn)
        txt3.draw(winn)
############################################################################################################
        yy = 30
        list_of_input_boxes = []
        for i in s:
            xx = 30
            for p in i:
                if p == 0:
                    input_box = Entry(Point(xx,yy),1)
                    input_box.setSize(25)
                    input_box.setFill(backgound)
                    input_box.setTextColor(z)
                    list_of_input_boxes.append(input_box.getAnchor())
                    input_box.draw(window)
                    pass
                else:
                    txt = Text(Point(xx,yy),p)
                    txt.setTextColor(z)
                    txt.setSize(25)
                    txt.draw(window)
                xx += 60
            yy += 60

        while True:
            clickity = winn.checkMouse()
            if clickity != None:
                if game.inside(clickity,Rectangle(Point(50, 10), Point(250, 80))):
                    print("ha")
                    break
                elif game.inside(clickity,Rectangle(Point(50, 100), Point(250, 170))):
                    winn.close()
                    window.close()
                    game.main_menu_window()
                    break
                elif game.inside(clickity,Rectangle(Point(50, 190), Point(250, 260))):
                    window.close()
                    winn.close()
                    break
                clickpoint = window.checkMouse()
            # for i in list_of_input_boxes:
            #     co_ord = Entry(list_of_input_boxes[i])
            #     for x in board:
            #         for j in x:
            #             if j == 0:
            #                 board[x][j] = int(co_ord.getText())

                ##############################################################################################


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
        the game. When finished, check board. """)
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
        for ii in game.buttons():
            ii.draw(win)
        x = 1
        aCircle = Circle(Point(60,500),10)
        while True:
            clickpoint = win.getMouse()
            aCircle.undraw()
            if game.inside(clickpoint,Rectangle(Point(40, 450), Point(120, 480))):
                x = 1
                aCircle = Circle(Point(80,500),10)
                aCircle.setFill(color_rgb(0,255,0))
                aCircle.draw(win)
            elif game.inside(clickpoint,Rectangle(Point(140, 450), Point(220, 480))):
                x = 2
                aCircle = Circle(Point(180,500),10)
                aCircle.setFill(color_rgb(0,255,0))
                aCircle.draw(win)
            elif game.inside(clickpoint,Rectangle(Point(240, 450), Point(320, 480))):
                x = 3
                aCircle = Circle(Point(280,500),10)
                aCircle.setFill(color_rgb(0,255,0))
                aCircle.draw(win)
            elif game.inside(clickpoint,Rectangle(Point(340, 450), Point(420, 480))):
                x = 4
                aCircle = Circle(Point(380,500),10)
                aCircle.setFill(color_rgb(0,255,0))
                aCircle.draw(win)
            elif game.inside(clickpoint,Rectangle(Point(440, 450), Point(520, 480))):
                x = 5
                aCircle = Circle(Point(480,500),10)
                aCircle.setFill(color_rgb(0,255,0))
                aCircle.draw(win)
            elif game.inside(clickpoint,Rectangle(Point(180, 520), Point(300, 550))):
                break
        win.close()
        game.initial_window(x)


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

game.main_menu_window()
