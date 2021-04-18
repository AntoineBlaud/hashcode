
import turtle as te
from constants import *;
from dessins import *;
import time



MAX_LOG = 20
log_printed = 0
player_hand = []
computer_hand = []
game = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}

te.setup(height=Height, width=Width)
te.setworldcoordinates(-Width / 2, 300, Width -
                        Width / 2, -Height + 300)
te.tracer(100)
te.pensize(1)
te.speed(10000)
te.bgcolor("white")
twrite = te.Turtle(visible=False)
pen = twrite.getpen()
twrite2 = te.Turtle(visible=False)
pen2 = twrite2.getpen()


def clear_area(coordinate_x, coordinate_y, length, width):
    te.up()
    te.goto(coordinate_x, coordinate_y)
    te.color("white")
    te.begin_fill()
    te.setheading(0)
    for i in range(2):
        te.fd(length)
        te.rt(90)
        te.fd(width)
        te.rt(90)
    te.end_fill()
    te.update()


def write_score(player, computer):
    global pen 
    goto = (-395 , -484)
    pen.penup()
    pen.goto(*goto)
    pen.pendown()
    pen.color("black")
    pen.write("Score: joueur {} | ordi {}".format(player, computer),  font=("Arial", 13, "normal"))
    pen.hideturtle()


def write_init_message():
    global pen 
    goto = (-200 , -300)
    pen.penup()
    pen.goto(*goto)
    pen.pendown()
    pen.write("Bienvenue dans le jeu Noe", font=("Arial", 25, "normal"))
    goto = (-120 , -260)
    pen.penup()
    pen.goto(*goto)
    pen.pendown()
    pen.write("Chargement en cours...", font=("Arial", 14, "normal"))

def write_log(log):
    global pen2 
    global log_printed
    pen2.color("black")
    if(log_printed > MAX_LOG):
        pen2.clear()
        log_printed = 0
    pos = pen2.pos()
    goto = (250 , -350 + log_printed * 10)
    pen2.penup()
    pen2.goto(*goto)
    pen2.pendown()
    pen2.write(log, font=("Arial", 7, "normal"))
    log_printed +=1

def get_input(text):
    return te.textinput("input", text)


def display_card(n, type, x, y, scale):

    if(n == -1):
        verso(x, y , scale)

    if(n == 0):
        if(type =="m"):
            perroquet_male(x, y , scale)
        if(type =="f"):
            perroquet_femelle(x, y , scale)

    if(n == 1):
        if(type =="m"):
            insecte_male(x, y , scale)
        if(type =="f"):
            insecte_femelle(x, y , scale)

    if(n == 2):
        if(type =="m"):
            chat_male(x, y , scale)
        if(type =="f"):
            chat_femelle(x, y , scale)
    if(n == 3):
        if(type =="m"):
            kangouroo_male(x, y , scale)
        if(type =="f"):
            kangouroo_femelle(x, y , scale)

    
    if(n == 4):
        if(type =="m"):
            panda_male(x, y , scale)
        if(type =="f"):
            panda_femelle(x, y , scale)

    if(n == 5):
        if(type =="m"):
            lion_male(x, y , scale)
        if(type =="f"):
            lion_femelle(x, y , scale)

    if(n == 6):
        if(type =="m"):
            ane_male(x, y , scale)
        if(type =="f"):
            ane_femelle(x, y , scale)

    if(n == 7):
        if(type =="m"):
            ours_male(x, y , scale)
        if(type =="f"):
            ours_femelle(x, y , scale)

    if(n == 8):
        if(type =="m"):
            girafe_male(x, y , scale)
        if(type =="f"):
            girafe_femelle(x, y , scale)

    if(n == 9):
        if(type =="m"):
            rino_male(x, y , scale)
        if(type =="f"):
            rino_femelle(x, y , scale)

    if(n == 10):
        if(type =="m"):
            elephant_male(x, y , scale)
        if(type =="f"):
            elephant_femelle(x, y , scale)


def display_barque():
    
    barque(250, -600, (0.05,0.05))
    te.penup()
    te.color("black")
    te.goto(-40, -280)
    te.pendown()
    te.write("A",font=("Arial", 15, "normal"))
    barque(50, -500, (0.05,0.05))
    te.penup()
    te.color("black")
    te.goto(-230, -180)
    te.pendown()
    te.write("B",font=("Arial", 15, "normal"))
    barque(450, -500, (0.05,0.05))
    te.penup()
    te.color("black")
    te.goto(150, -180)
    te.pendown()
    te.write("C",font=("Arial", 15, "normal"))
    barque(150, -350, (0.05,0.05))
    te.penup()
    te.color("black")
    te.goto(-140, -30)
    te.pendown()
    te.write("D",font=("Arial", 15, "normal"))
    barque(350, -350, (0.05,0.05))
    te.penup()
    te.color("black")
    te.goto(60, -30)
    te.pendown()
    te.write("E",font=("Arial", 15, "normal"))


def display_game_card(boatid, index, n, type):
    if(boatid == "A"):
        x, y = (250 + 40*index), -720
        display_card(n, type, x, y, (0.03,0.03))
    if(boatid == "B"):
        x, y = (50 + 40*index), -625
        display_card(n, type, x, y, (0.03,0.03))
    if(boatid == "C"):
        x, y = (450 + 40*index), -625
        display_card(n, type, x, y, (0.03,0.03))
    if(boatid == "D"):
        x, y = (150 + 40*index), -480
        display_card(n, type, x, y, (0.03,0.03))
    if(boatid == "E"):
        x, y = (350 + 40*index), -480
        display_card(n, type, x, y, (0.03,0.03))


def display_player_cards(cards):
    for i,card  in enumerate(cards):
        x, y = (0 + i*80) , -100
        display_card(card[0],card[1], x , y, (0.08, 0.08))
        player_hand.append(card)
        te.update()


def update_player_cards(cards):
    for i,card  in enumerate(player_hand):
        if(card not in cards ):
            clear_player_card(i)


def update_computer_cards(cards):
    for i,card  in enumerate(computer_hand):
        if(card not in cards ):
            clear_computer_card(i)
        


def clear_player_card(index):
   
    x, y = (-400 + index * 80) , 300
    clear_area(x, y, 78, 115)


def display_computer_cards(cards):
    for i,card  in enumerate(cards):
        x, y = (720 - i*80) , -780
        display_card(-1, "", x , y, (0.08, 0.08))
        computer_hand.append(card)
        te.update()

def clear_computer_card(index):
    x, y = (400 - 80*index) , -380
    clear_area(x, y, 78, 115)


def clear():
    pen.clear()


def display_jeu(jeu : dict):
    for boatid in jeu.keys():
        boat_content = jeu[boatid]
        for i, card in enumerate(boat_content):
            if card not in game[boatid]:
                game[boatid].append(card)
                display_game_card(boatid, i, card[0], card[1])

def display_main(main):
    pass

def init():

    write_init_message()
    plage(0, 0,(0.20,0.20))
    display_barque()
   
