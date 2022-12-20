import sys
import time
import random
import itertools
from equipment import adventure, end, d, quest, title, table, hd, area1, area2, area3, area4, area5, area6, area7, area8, area9, area10, area11, area12, area13, area14, area15, start, area50, area5r, area6r, area7r, area9r, area10r, area11r, area12r, area14r, fin, dra, HEAD, big_dragon, pfight, fire
from message import msg1, msg2, msg3


print(adventure)
time.sleep(2)
sys.stdout.write("\033[7F")
print(quest)
time.sleep(2)
sys.stdout.write("\033[30F")
print(title)
tyms = 0
play = ""
while play != "n":
    if tyms > 0:
        print("\n\n\n\n\n\n\n\nSTART...")
    tyms += 1
    box1 = ""
    box2 = ""
    box3 = ""
    box4 = ""
    box5 = ""
    box6 = ""
    box7 = ""
    box8 = ""
    box9 = ""
    box10 = ""
    box11 = ""
    box12 = ""
    box13 = ""
    box14 = ""
    box15 = ""

    box = [1, 2, 3, 4, 5, 6, 7, 8,
           9, 10, 11, 12, 13, 14, 15]
    block = [", shield", ", staff", ", potions", ", grimoire",
             ", armor", " slime", " undead", " gold", " gem"]
    while block != []:
        b1 = random.choice(block)
        index1 = block.index(b1)
        block.pop(index1)
        block = block

        bx = random.choice(box)
        index2 = box.index(bx)
        box.pop(index2)
        box = box
        if bx == 1:
            box1 = b1
        elif bx == 2:
            box2 = b1
        elif bx == 3:
            box3 = b1
        elif bx == 4:
            box4 = b1
        elif bx == 5:
            box5 = b1
        elif bx == 6:
            box6 = b1
        elif bx == 7:
            box7 = b1
        elif bx == 8:
            box8 = b1
        elif bx == 9:
            box9 = b1
        elif bx == 10:
            box10 = b1
        elif bx == 11:
            box11 = b1
        elif bx == 12:
            box12 = b1
        elif bx == 13:
            box13 = b1
        elif bx == 14:
            box14 = b1
        elif bx == 15:
            box15 = b1
    #     print(bx,b1)
    # print(box1,box11,box5,box8)

    time.sleep(3)
    sys.stdout.write("\033[6E")
    print(table)
    time.sleep(1)
    sys.stdout.write("\033[38F")
    print(msg1)
    print("\033[5F"+hd)
    time.sleep(5)
    sys.stdout.write("\033[8F")
    print(msg3)
    print("\033[5F"+hd)
    # ---------------------------------------------------------------READY ALL TO START
    time.sleep(1)
    sys.stdout.write("\033[3E")
    commamd_area = "\033[32m⢸⡇⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[33m𝟙𝟙\033[32m⠀⡬⣿⠃⠀⠀⠀⠀⠀⠙⢿⣶⡆⣀⠀⠀⠀⠀⠀⠀⠀⠋⡟⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣤⢀⣰⣽⡿⠾⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⡴⠶⣶⠶⣶⠶⢶⠶⢤⣤⣄⡀                             "
    input(commamd_area + "\033[33mPRESS ENTER TO START... ")
    sys.stdout.write("\033[18E")
    print(start)
    position = 0
    B = "\033[37m"
    T = "\033[37msword"
    P = 0
    M = ""
    sp = " " * 14
    gl = " " * 5
    gm = " " * 4
    move = ""
    c = 3       
    LIFE = "\033[41m    "
    L = 1

    bot = f"""\033[32m⠀⠘⢷⡀⠀⠀ ⠀\033[33m🆂 🆃 🅰 🆁 🆃 ...\033[32m⢸⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢼⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⣿⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣉⣿⣀⠀⠀⠀⠀⠀⢀⡀⠰⣦⣽⠟⠁⠀⠀⠀⠀      \033[33mPOSITION:\033[37m {P}\033[32m⠀⠀ ⠀          {sp}\033[33mBAG:\033[37m{B}\033[32m            {gm}{gl}  \033[33m LIFE: {LIFE}\033[49m\033[32m
⠀⠀⠈⠿⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⢸⣧⡄⢠⡄⢠⡄⠠⠄⠠⠤⠠⠄⢠⣤⣀⣶⣼⣷⣆⣰⣆⣀⣶⣀⣶⣆⣰⣆⣰⣶⣰⣆⣆⣿⣶⠀⠤⠀⣤⠀⣀⠀⣀⠀⠀⠀⠀⠀⠀⠀⢉⢻⢉⡀⢠⡄⣰⣦⣬⡷⠟⠉⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀ ⠀  \033[33mCHANCE:\033[37m {c}\033[32m                      \033[33m TREASURE: {T}\033[32m
    ⠙⢿⣶⣶⣦⣤⣤⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⠛⠛⠛⢻⣶⣿⣦⣭⣤⣿⣤⣽⣥⣿⣤⣼⣼⣿⣷⡿⠟⠋⠁                                                    \033[33m MONSTER:\033[36m{M}"""
    print("\033[F"+bot)
    move = input("\033[26F" + commamd_area +
                 "\033[33mPRESS '1' TO MOVE ONE SPACE OR 'ENTER' TO ROLL DICE... ")

    # -------------------------------------------------------START

    def go():

        dice_number = ['''\x1b[31m    ┏┓  
    ┏┛┃  
    ┗┓┃    
     ┃┃   
    ┏┛┗┓  
    ┗━━┛ ''',
                       '''\x1b[32m   ╔═══╗
    ║╔═╗║
    ╚╝╔╝║
    ╔╗╚╗║
    ║╚═╝║
    ╚═══╝''',
                       '''\x1b[36m    ┏┓  
    ┏┛┃  
    ┗┓┃  
     ┃┃  
    ┏┛┗┓  
    ┗━━┛ ''',
                       '''\x1b[33m   ┏━━━┓
    ┃┏━┓┃
    ┗┛┏┛┃
    ┏━┛┏┛
    ┃┃┗━┓
    ┗━━━┛''',
                       '''\x1b[34m    ┏┓  
    ┏┛┃   
    ┗┓┃  
     ┃┃  
    ┏┛┗┓  
    ┗━━┛ ''',
                       '''\x1b[35m   ┏━━━┓
    ┃┏━┓┃
    ┗┛┏┛┃
    ┏━┛┏┛
    ┃┃┗━┓
    ┗━━━┛''',
                       '''\x1b[30m   ╔═══╗
    ║╔═╗║
    ╚╝╔╝║
    ╔╗╚╗║
    ║╚═╝║
    ╚═══╝''']

    # ---------------------------------------------def roll_dice():

        numbers = [1, 2, 3, 4, 5, 6]
        y = random.choice(numbers)

        display = itertools.cycle(dice_number)
        max_width = max(map(len, dice_number))
        if y == 1:
            ran = 1
            n = 12  # 1
        elif y == 2:
            ran = 2
            n = 18  # 2
        elif y == 3:
            ran = 1
            n = 15  # 1
        elif y == 4:
            ran = 2
            n = 13  # 2
        elif y == 5:
            ran = 3
            n = 16  # 3
        else:
            ran = 3
            n = 14  # 3

        x = 0
        while True:
            print('\033[6F', next(display).ljust(max_width))
            time.sleep(.1)
            x += 1
            if x == n:
                break
        return ran

    # -------------------------------------------move

    while position <= 15:

        if position == 0:
            sys.stdout.write('\033[19E')
        else:
            sys.stdout.write('\033[F')

        
        if c != 0:
            if move == '1':
                k = 1
                move = ""
                c -= 1                  
            else:
                k = go()
        else:
            k = go()

        position += k
        P += k
        if position > 9:
            sp = " " * 13
        elif position > 15:
            P = "CASTLE"
            sp = " " * 9

        # --------------------------------------------------resources
        if position == 1:
            if box1 != "":
                if box1 == " gold" or box1 == " gem":
                    B = box1
                    L += 1
                    if box1 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box1 == " undead" or box1 == " slime":
                    if box1 == " undead":
                        un = ""
                    elif box1 == " slime":
                        sl = ""
                    L -= 1
                    M = box1
                else:
                    T += box1
                    L += 1
        elif position == 2:
            if box2 != "":
                if box2 == " gold" or box2 == " gem":
                    B += box2
                    L += 1
                    if box2 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box2 == " undead" or box2 == " slime":
                    if box2 == " undead":
                        un = ""
                    elif box2 == " slime":
                        sl = ""
                    M += box2
                    L -= 1
                else:
                    T += box2
                    L += 1
        elif position == 3:
            if box3 != "":
                if box3 == " gold" or box3 == " gem":
                    B += box3
                    L += 1
                    if box3 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box3 == " undead" or box3 == " slime":
                    if box3 == " undead":
                        un = ""
                    elif box3 == " slime":
                        sl = ""
                    M += box3
                    L -= 1
                else:
                    T += box3
                    L += 1
        elif position == 4:
            if box4 != "":
                if box4 == " gold" or box4 == " gem":
                    B += box4
                    L += 1
                    if box4 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box4 == " undead" or box4 == " slime":
                    if box4 == " undead":
                        un = ""
                    elif box4 == " slime":
                        sl = ""
                    M += box4
                    L -= 1
                else:
                    T += box4
                    L += 1
        elif position == 5:
            if box5 != "":
                if box5 == " gold" or box5 == " gem":
                    B += box5
                    L += 1
                    if box5 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box5 == " undead" or box5 == " slime":
                    if box5 == " undead":
                        un = ""
                    elif box5 == " slime":
                        sl = ""
                    M += box5
                    L -= 1
                else:
                    T += box5
                    L += 1
        elif position == 6:
            if box6 != "":
                if box6 == " gold" or box6 == " gem":
                    B += box6
                    L += 1
                    if box6 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box6 == " undead" or box6 == " slime":
                    if box6 == " undead":
                        un = ""
                    elif box6 == " slime":
                        sl = ""
                    M += box6
                    L -= 1
                else:
                    T += box6
                    L += 1
        elif position == 7:
            if box7 != "":
                if box7 == " gold" or box7 == " gem":
                    B += box7
                    L += 1
                    if box7 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box7 == " undead" or box7 == " slime":
                    if box7 == " undead":
                        un = ""
                    elif box7 == " slime":
                        sl = ""
                    M += box7
                    L -= 1
                else:
                    T += box7
                    L += 1
        elif position == 8:
            if box8 != "":
                if box8 == " gold" or box8 == " gem":
                    B += box8
                    L += 1
                    if box8 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box8 == " undead" or box8 == " slime":
                    if box8 == " undead":
                        un = ""
                    elif box8 == " slime":
                        sl = ""
                    M += box8
                    L -= 1
                else:
                    T += box8
                    L += 1
        elif position == 9:
            if box9 != "":
                if box9 == " gold" or box9 == " gem":
                    B += box9
                    L += 1
                    if box9 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box9 == " undead" or box9 == " slime":
                    if box9 == " undead":
                        un = ""
                    elif box9 == " slime":
                        sl = ""
                    M += box9
                    L -= 1
                else:
                    T += box9
                    L += 1
        elif position == 10:
            if box10 != "":
                if box10 == " gold" or box10 == " gem":
                    B += box10
                    L += 1
                    if box10 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box10 == " undead" or box10 == " slime":
                    if box10 == " undead":
                        un = ""
                    elif box10 == " slime":
                        sl = ""
                    M += box10
                    L -= 1
                else:
                    T += box10
                    L += 1
        elif position == 11:
            if box11 != "":
                if box11 == " gold" or box11 == " gem":
                    B += box11
                    L += 1
                    if box11 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box11 == " undead" or box11 == " slime":
                    if box11 == " undead":
                        un = ""
                    elif box11 == " slime":
                        sl = ""
                    M += box11
                    L -= 1
                else:
                    T += box11
                    L += 1
        elif position == 12:
            if box12 != "":
                if box12 == " gold" or box12 == " gem":
                    B += box12
                    L += 1
                    if box12 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box12 == " undead" or box12 == " slime":
                    if box12 == " undead":
                        un = ""
                    elif box12 == " slime":
                        sl = ""
                    M += box12
                    L -= 1
                else:
                    T += box12
                    L += 1
        elif position == 13:
            if box13 != "":
                if box13 == " gold" or box13 == " gem":
                    B += box13
                    L += 1
                    if box13 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box13 == " undead" or box13 == " slime":
                    if box13 == " undead":
                        un = ""
                    elif box13 == " slime":
                        sl = ""
                    M += box13
                    L -= 1
                else:
                    T += box13
                    L += 1
        elif position == 14:
            if box14 != "":
                if box14 == " gold" or box14 == " gem":
                    B += box14
                    L += 1
                    if box14 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box14 == " undead" or box14 == " slime":
                    if box14 == " undead":
                        un = ""
                    elif box14 == " slime":
                        sl = ""
                    M += box14
                    L -= 1
                else:
                    T += box14
                    L += 1
        elif position == 15:
            if box15 != "":
                if box15 == " gold" or box15 == " gem":
                    B += box15
                    L += 1
                    if box15 == " gold":
                        gl = ""
                    else:
                        gm = ""
                elif box15 == " undead" or box15 == " slime":
                    if box15 == " undead":
                        un = ""
                    elif box15 == " slime":
                        sl = ""
                    M += box15
                    L -= 1
                else:
                    T += box15
                    L += 1
        if L == 1:
            LIFE = L * "\033[41m    "
        elif L <= 3:
            LIFE = L * "\033[43m    "
        else:
            LIFE = L * "\033[42m    "
        
        if c == 0:
            c1="\33[31mNO CHANCE LEFT!"
            c3=""
        else:
            c1=c
            c3=" "*14
        print(f"""\033[3E\033[32m⠀⠘⢷⡀⠀⠀ ⠀\033[33m🆂 🆃 🅰 🆁 🆃 ...\033[32m⢸⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢼⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⣿⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣉⣿⣀⠀⠀⠀⠀⠀⢀⡀⠰⣦⣽⠟⠁⠀⠀⠀⠀      \033[33mPOSITION:\033[37m {P}\033[32m⠀⠀ ⠀          {sp}\033[33mBAG:\033[37m{B}\033[32m            {gm}{gl}  \033[33m LIFE: {LIFE}\033[49m\033[32m                   
⠀⠀⠈⠿⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⢸⣧⡄⢠⡄⢠⡄⠠⠄⠠⠤⠠⠄⢠⣤⣀⣶⣼⣷⣆⣰⣆⣀⣶⣀⣶⣆⣰⣆⣰⣶⣰⣆⣆⣿⣶⠀⠤⠀⣤⠀⣀⠀⣀⠀⠀⠀⠀⠀⠀⠀⢉⢻⢉⡀⢠⡄⣰⣦⣬⡷⠟⠉⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀ ⠀  \033[33mCHANCE:\033[37m {c1}\033[32m{c3}        \033[33m TREASURE: {T}\033[32m
    ⠙⢿⣶⣶⣦⣤⣤⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⠛⠛⠛⢻⣶⣿⣦⣭⣤⣿⣤⣽⣥⣿⣤⣼⣼⣿⣷⡿⠟⠋                                                     \033[33m MONSTER:\033[36m{M}""")

        # -----------------------------------------movement
        if position == 1:
            print("\033[7F", area1)
            sys.stdout.write('\033[4F')
        elif position == 2:
            print("\033[7F", area2)
            sys.stdout.write('\033[4F')
        elif position == 3:
            print("\033[7F", area3)
            sys.stdout.write('\033[4F')
        elif position == 4:
            print("\033[7F", area4)
            sys.stdout.write('\033[4F')
        elif position == 5:
            print("\033[7F", area50)
            print("\033[14F", area5)
            sys.stdout.write('\033[5E')
        elif position == 6:
            print("\033[7F", area50)
            print("\033[14F", area5r)
            if k == 1:
                print("\033[12F", area6)
            else:
                print("\033[12F", area6)
            sys.stdout.write('\033[12E')
        elif position == 7:
            if k == 1:
                print("\033[23F", area6r)
                print("\033[4F", area7)
            elif k == 2:
                print("\033[16F", area5r)
                print("\033[11F", area7)
            else:
                print("\033[7F", area50)
                print("\033[14F", area5r)
                print("\033[11F", area7)
            sys.stdout.write('\033[11E')
        elif position == 8:
            if k == 3:
                print("\033[16F", area5r)
                print("\033[7F", area8)
            elif k == 2:
                print("\033[23F", area6r)
                print(area8)
            else:
                print("\033[22F", area7r)
                print("\033[F", area8)
            sys.stdout.write('\033[7E')
        elif position == 9:
            if k == 3:
                print("\033[23F", area6r)
                print(area9)
            elif k == 2:
                print("\033[22F", area7r)
                print("\033[F", area9)
            else:
                print("\033[18F", area9)
            sys.stdout.write('\033[7E')
        elif position == 10:
            if k == 3:
                print("\033[22F", area7r)
                print("\033[F", area10)
            elif k == 2:
                print("\033[18F", area9r)
                print("\033[5F", area10)
            else:
                print("\033[18F", area9r)
                print("\033[5F", area10)
            sys.stdout.write('\033[7E')
        elif position == 11:
            if k == 3:
                print("\033[18F", area9r)
                print("\033[13F", area11)
            elif k == 2:
                print("\033[18F", area9r)
                print("\033[13F", area11)
            else:
                print("\033[18F", area10r)
                print("\033[13F", area11)
            sys.stdout.write('\033[15E')
        elif position == 12:
            if k == 3:
                print("\033[18F", area9r)
                print("\033[22F", area12)
            elif k == 2:
                print("\033[18F", area10r)
                print("\033[22F", area12)
            else:
                print("\033[26F", area11r)
                print("\033[14F", area12)
            sys.stdout.write('\033[24E')
        elif position == 13:
            if k == 3:
                print("\033[18F", area10r)
                print("\033[18F", area13)
            elif k == 2:
                print("\033[26F", area11r)
                print("\033[10F", area13)
            else:
                print("\033[35F", area12r)
                print("\033[F", area13)
            sys.stdout.write('\033[20E')
        elif position == 14:
            if k == 3:
                print("\033[26F", area11r)
                print("\033[10F", area14)
            elif k == 2:
                print("\033[35F", area12r)
                print("\033[F", area14)
            else:
                print("\033[31F", area14)
            sys.stdout.write('\033[20E')
        elif position == 15:
            if k == 3:
                print("\033[35F", area12r)
                print("\033[3F", area15)
            elif k == 2:
                print("\033[31F", area14r)
                print("\033[7F", area15)
            else:
                print("\033[31F", area14r)
                print("\033[7F", area15)
            sys.stdout.write('\033[22E')
        elif position > 15:
            if k == 2 or k == 3:
                print("\033[31F", area14r)
                print("\033[7F", fin)
            else:
                print("\033[33F", fin)
            sys.stdout.write('\033[22E')

        if LIFE == "":
            break
        elif position <= 15:
            move = input("\033[20F" + commamd_area +
                         "\033[33mPRESS '1' TO MOVE ONE SPACE OR 'ENTER' TO ROLL DICE... ")
            if position >= 1:
                sys.stdout.write('\033[20E')

    if LIFE == "":
        time.sleep(1)
        print("\033[31F"+msg2)
        print("\033[15F"+dra)
        print("\033[11F"+HEAD)
        print("\033[9F", fin)
        print("\n\n"+commamd_area +
              "\033[31mYOU'VE RUN OUT OF LIFE......             .                    ")
    else:
        time.sleep(1)
        print("\033[31F"+msg2)
        print("\033[15F"+dra)
        print("\033[11F"+HEAD)
        print("\033[9F", fin)
        if L <= 3:
            print("\n\n"+commamd_area +
                  "\033[31mNOT ENOUGH LIFE.......                                    ")
        else:
            print("\n\n"+commamd_area +
                  "\033[32mYOU ARE VICTORIOUS.......                               ")

    # # ---------------------------------------------------battle
    time.sleep(3)
    print("\033[45E")
    if L <= 3 or LIFE == "":
        print(d)
    elif L > 3:
        print("\033[7E"+big_dragon)
        print("\033[28F"+fire)
        time.sleep(3)
        print("\033[10F"+pfight)
        print("\033[55F"+end)
    play = input(
        "\033[33m\033[52EPLAY AGAIN?\033[37m \nIf YES press \033[32mENTER\033[37m, \nIf NO press \033[31m'n'\033[37m: ").lower()

print("\x1b[45E")
