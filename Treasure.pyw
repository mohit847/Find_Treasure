# from pathlib import WindowsPath
import tkinter
from tkinter import *
from tkinter.font import BOLD
from PIL import Image,ImageDraw,ImageTk
from tkinter import messagebox
import os
from tkinter import simpledialog
from tkinter import Tk, Label, Button

top =Tk()
top.iconbitmap("icon.ico")
top.title("Treasure Game")
top.geometry("1000x780")
top.minsize(1000,780)
top.maxsize(1000,780)

def startpress():
    lablname.destroy()
    labelimage.destroy()
    labeltext.destroy()
    btnstart.destroy()
    lblInstruction.destroy()
    labln.destroy()
    my_canvas.destroy()
    welcome()

#################### Home page map image #######################
bg=PhotoImage(file="home2.png")
my_canvas= Canvas(top,width=1000, height=1080)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=bg, anchor="nw")

img1 = PhotoImage(file="1st_img.png")
labelimage = Label(top, image=img1,bg='#fde5c4')
labelimage.place(x=450,y=60)

labeltext = Label(top, text="Treasur Hunt", font=("comic sans MS", 25, "bold"),bg='#fde5c4')
labeltext.place(x=470, y=250)

img2 = (Image.open("start1.png"))
resized_image= img2.resize((200,200), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

global name
lablname=Label(top,text="Enter your name to play the game ",font=("Berlin Sans FB", 20, "bold"),bg='#fde5c4')
lablname.place(x=280,y=350)
labln=Label(top,text="Your Name  ",font=("Berlin Sans FB", 20, "bold"),bg='#fde5c4')
labln.place(x=280,y=400)
name=Entry(top,font=( 20),border=3,bg='#fde5c4')
name.place(x=480,y=405)

#start button 
btnstart = Button(top, image=new_image, relief=FLAT, border=0,height = 200, width = 200 ,command=startpress,bg='#fde5c4')
btnstart.place(x=400,y=520)


def change_color():
    current_color = lblInstruction.cget("fg")
    next_color = "green" if current_color == "red" else "red"
    lblInstruction.config(fg=next_color)
    top.after(1000, change_color)

lblInstruction = Label(top,text="Click Play once Yor are ready",font=("consolas", 20),justify="center",bg='#fde5c4',fg='red')
lblInstruction.place(x=280,y=470)
change_color()

####### HOVER GUN ###########
def btn_enter1(event):
    gun.config(bg="black", fg="gold")
    status1.config(text='A gun which is having only one bullet with this gun \n you can only kill one monster or one zombie',bg='#fde5c4')

def btn_leave1(event):
    gun.config(bg="green", fg="black")
    status1.config(text='',bg='#fde5c4')

status1 = Label(top,font=('arial',15,'bold'),fg='red3',bg='#fde5c4')
status1.place(x=220,y=650)

############ HOVER SWARD ############
def btn_enter2(event):
    sward.config(bg="black", fg="gold")
    status2.config(text='A sward with which you can only cut roots and branches of trees, \n you cannot cut grasses and flowers with this sward',bg='#fde5c4')

def btn_leave2(event):
    sward.config(bg="gray", fg="black")
    status2.config(text='',bg='#fde5c4')

status2 = Label(top,font=('arial',15,'bold'),fg='red3',bg='#fde5c4')
status2.place(x=220,y=650)

############ HOVER BOMB ############
def btn_enter4(event):
    bomb.config(bg="black", fg="gold")
    status4.config(text='You can use this bomb to kill more than 10 enemy \n if you will use it to kill only one enemy than it will be wasted \n you can only use this bomb if you are not wasting it ',bg='#fde5c4')

def btn_leave4(event):
    bomb.config(bg="red", fg="black")
    status4.config(text='',bg='#fde5c4')

status4 = Label(top,font=('arial',15,'bold'),fg='red3',bg='#fde5c4')
status4.place(x=220,y=650)

############ HOVER KNIFE ############
def btn_enter3(event):
    Knife.config(bg="black", fg="gold")
    status3.config(text='This knife is only used to cut the small grasses , flowers and leaves ',bg='#fde5c4')

def btn_leave3(event):
    Knife.config(bg="blue", fg="black")
    status3.config(text='',bg='#fde5c4')

status3 = Label(top,font=('arial',15,'bold'),fg='red3',bg='#fde5c4')
status3.place(x=220,y=650)


################### EXIT FROM GAME ############
def exit():
    top.destroy()

################# RESTART GAME ###############
def restart():
    top.destroy()
    os.startfile("index.pyw")

############## CHECK TREASURE UNLOCKED OR NOT #############
def check():
    
    global e1
    string = int(e1.get()) 
    if string==3:
        your_answer.destroy()
        question_1.destroy()
        e1.destroy()
        question.destroy()
        cnf.destroy()
        found = Label(top, text="congratulation You unlocked the treasure ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        found.pack(pady=(100, 0)) 

        exit_restart= Label(top, text="Do you want to play again ? ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        exit_restart.pack(pady=(80, 50)) 

        restart_game = tkinter.Button(top,text="Restart",border=2,font=(20),height= 2, width=10,fg = "white",bg = "red",command=restart)
        restart_game.place(x=300,y=300)

        exit_game = tkinter.Button(top, text="Exit", border=2,font=(20),height= 2, width=10,fg = "white",bg = "Green",command=exit)
        exit_game.place(x=500,y=300)
    else:
        question_1.destroy()
        your_answer.destroy()
        e1.destroy()
        question.destroy()
        cnf.destroy()
        not_found = Label(top, text="You answered wrong you loose  ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        not_found.pack(pady=(100, 0))

        exit_restart= Label(top, text="Do you want to play again ? ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        exit_restart.pack(pady=(80, 50)) 

        restart_game = tkinter.Button(top,text="Restart",border=2,font=(20),height= 2, width=10,fg = "white",bg = "red",command=restart)
        restart_game.place(x=300,y=300)

        exit_game = tkinter.Button(top, text="Exit", border=2,font=(20),height= 2, width=10,fg = "white",bg = "Green",command=exit)
        exit_game.place(x=500,y=300)
             
################ QUESTION TO UNLOCK TREASURE ##################
def qus1():
    global question_1
    global cnf
    global e1
    global your_answer
    question_1 = Label(top, text="Knife was placed at which Number 1,2,3,4 ?", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
    question_1.pack(pady=(0, 50))  

    your_answer = Label(top, text="Your Answer ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
    your_answer.place(x=100,y=375)  
    e1 =tkinter.Entry(top,font=( 20),border=2,bg='#fde5c4')
    e1.pack(pady=(0,0))
    cnf = tkinter.Button(top,text="Check Answer",border=2,font=(15),height= 2, width=17,fg = "white",bg = "red",command=lambda: [check()])
    cnf.pack(pady=(100, 100)) 


################## CONFIRMATION OF TOOL SELECTION #############
def stage1():
    global USER_INP
    USER_INP = simpledialog.askstring(title="Confirmation",
                                      prompt="Confirm which tool you have selected 1,2,3,4 ? ")       

################## CONFIRMATION OF ENEMY SELECTION #############
def stage2():
    global USER
    USER = simpledialog.askstring(title="Confirmation",
                                  prompt="Confirm which obstacle you have selected 1,2,3,4 ? ")      

################## TREASURE FOUND OR NOT #########################
def result():
    global question
    global wrong_answer
    global label_win
    global label_loose
    if USER_INP==USER:
        question = Label(top, text="HURRY!! \n You found the treasure ! \n \n Now you have to answer the question \n to unlock the treasure", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        question.pack(pady=(50, 50)) 
        qus1() 

    elif USER=="":
        question_blank = Label(top, text="You have not answered. ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        question_blank.pack(pady=(50, 50)) 

        exit_restart= Label(top, text="Do you want to play again ? ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        exit_restart.pack(pady=(80, 50)) 

        restart_game = tkinter.Button(top,text="Restart",border=2,font=(20),height= 2, width=10,fg = "white",bg = "red",command=restart)
        restart_game.place(x=300,y=300)

        exit_game = tkinter.Button(top, text="Exit", border=2,font=(20),height= 2, width=10,fg = "white",bg = "Green",command=exit)
        exit_game.place(x=500,y=300)
       

    else:
        wrong_answer = Label(top, text="SORRY!! \n YOU ANSWERED WRONG",font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        wrong_answer.pack(pady=(50, 0))

        exit_restart= Label(top, text="Do you want to play again ? ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        exit_restart.pack(pady=(80, 50)) 

        restart_game = tkinter.Button(top,text="Restart",border=2,font=(20),height= 2, width=10,fg = "white",bg = "red",command=restart)
        restart_game.place(x=300,y=300)

        exit_game = tkinter.Button(top, text="Exit", border=2,font=(20),height= 2, width=10,fg = "white",bg = "Green",command=exit)
        exit_game.place(x=500,y=300)

################ DESTROY ENEMY BUTTONS AND LABELS ####################
def last():
    global conti
    beast.destroy()
    tree_Branches.destroy()
    zombies.destroy()
    poisonous_flowers.destroy()
    lblright2.destroy()
    s2.destroy()
    no11.destroy()
    no22.destroy()
    no33.destroy()
    no44.destroy()


##################### ENEMY BUTTONS ###################
def select():
    gun.destroy()
    sward.destroy()
    Knife.destroy()
    bomb.destroy()
    no1.destroy()
    no2.destroy()
    no3.destroy()
    no4.destroy()
    lblright1.destroy()
    s1.destroy()
    lbldetail.destroy()
    global lblright2
    global beast
    global tree_Branches
    global zombies
    global poisonous_flowers
    global no11
    global no22
    global no33
    global no44
    global s2
    if USER_INP=="":
        question_blank = Label(top, text="You have not answered. ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        question_blank.pack(pady=(50, 50)) 

        exit_restart= Label(top, text="Do you want to play again ? ", font=("Copperplate Gothic Bold", 25, "bold"),bg='#fde5c4')
        exit_restart.pack(pady=(80, 50)) 

        restart_game = tkinter.Button(top,text="Restart",border=2,font=(20),height= 2, width=10,fg = "white",bg = "red",command=restart)
        restart_game.place(x=300,y=300)

        exit_game = tkinter.Button(top, text="Exit", border=2,font=(20),height= 2, width=10,fg = "white",bg = "Green",command=exit)
        exit_game.place(x=500,y=300)

    else:
        s2 = Label(top,text=" STAGE 2 ",font=("Times", 22),fg="#000000",bg='#fde5c4')  # FACA2F
        s2.place(x=100, y=30)
        lblright2 = Label(top,text="To move futher you have to make your way by using tool with you \n kill zombies or a beast, cut the poisonous flowers or the branches of tree  ",font=("Times", 20),fg="#000000",bg='#fde5c4')  # FACA2F
        lblright2.place(x=100, y=80)
        lblright1.destroy()
        beast = tkinter.Button(top,text="Beast",border=2,font=(20),height= 5, width=20,fg = "white",bg = "red",command=lambda: [last(),stage2(),result()])
        beast.place(x=200,y=200)
        no11= Label(top,text=" 1 \n A Dangerous beast is on the way.",font=("Times", 14),fg="#000000",bg='#fde5c4')  # FACA2F
        no11.place(x=200,y=350)

        tree_Branches = tkinter.Button(top, text="Tree Branches", border=2,font=(20),height= 5, width=20,fg = "white",bg = "Green",command=lambda: [last(),stage2(),result()])
        tree_Branches.place(x=200,y=500)
        no22 = Label(top,text=" 2 \n Lot of branches are there on the way.",font=("Times", 14),fg="#000000",bg='#fde5c4')  # FACA2F
        no22.place(x=200,y=650)

        poisonous_flowers = tkinter.Button(top, text="Poisonous flowers", border=2,font=(20),height= 5, width=20,fg = "white",bg = "blue",command=lambda: [last(),stage2(),result()])
        poisonous_flowers.place(x=500,y=200)
        no44 = Label(top,text=" 3 \n poisonous flowers are on the way. ",font=("Times", 14),fg="#000000",bg='#fde5c4')  # FACA2F
        no44.place(x=500,y=350)

        zombies = tkinter.Button(top, text="Zombies", border=2,font=(20),height= 5, width=20,fg = "white",bg = "gray",command=lambda: [last(),stage2(),result()])
        zombies.place(x=500,y=500)
        no33 = Label(top,text=" 4 \n 10 zombies are on the way ",font=("Times", 14),fg="#000000",bg='#fde5c4')  # FACA2F
        no33.place(x=500,y=650)

        

def welcome():
    top.configure(bg='#fde5c4')
    global ppname
    global name
    global wel
    global start_message
    global labl_Hint
    
    
    pname = name.get()
    ppname=Label(top, text=f'Welcome to the Treasure,{pname.upper()}',font=("Bahnschrift SemiBold SemiConden",30),bg='#fde5c4')
    ppname.pack(pady=(100,0))

    start_message = Label(top,text=" You have to find out the treasure by crossing all the stages ahead. ",font=("Times", 20),fg="#000000",bg='#fde5c4')  # FACA2F
    start_message.place(x=100, y=200)

    labl_Hint = Label(top,text=" Hint : Remember all the stages to find out the treasure. ",font=("Times", 15),fg="red",bg='#fde5c4')  # FACA2F
    labl_Hint.place(x=100, y=450)
    name.destroy()
    wel = Button(top,text=" Continue ",border=2,font=(20),height= 3, width=20,fg = "white",bg = "green",command=play)
    wel.place(x=350,y=300)

    
######################## TOOLS BUTTONS ###################
def play():
    labl_Hint.destroy()
    ppname.destroy()
    wel.destroy()
    start_message.destroy()
    global lblright1    
    global lbldetail
    global s1
    s1 = Label(top,text=" STAGE 1 ",font=("Times", 22),fg="#000000",bg='#fde5c4')  # FACA2F
    s1.place(x=100, y=30)

    lblright1 = Label(top,text="Before moving further choose one tool \n which will help you in finding the treasure  ",font=("Times", 20),fg="#000000",bg='#fde5c4')  # FACA2F
    lblright1.place(x=230, y=80)
    global gun
    global sward
    global bomb
    global Knife
    global no1
    global no2
    global no3
    global no4

    lbldetail = Label(top,text=" Hover on tool to get the uses of tool ",font=("Times", 15,),fg = "red",bg='#fde5c4')  # FACA2F
    lbldetail.place(x=300, y=160)

    gun = Button(top,text="Gun",border=2,font=(20),height= 5, width=20,fg = "white",bg = "green",command=lambda: [stage1(),select()])
    gun.place(x=200,y=200)
    gun.bind("<Enter>",btn_enter1)
    gun.bind("<Leave>",btn_leave1)
    no1= Label(top,text=" 1 \n Gun with one bullet.",font=("Times", 14),bg='#fde5c4')  # FACA2F
    no1.place(x=230,y=350)

    sward = Button(top, text="Sward", border=2,font=(20),height= 5, width=20,fg = "white",bg = "Gray",command=lambda: [stage1(),select()])
    sward.place(x=200,y=430)
    sward.bind("<Enter>",btn_enter2)
    sward.bind("<Leave>",btn_leave2)
    no2 = Label(top,text=" 2 \n A sharp sward.",font=("Times", 14),bg='#fde5c4')  # FACA2F
    no2.place(x=230,y=570)
 
    Knife = Button(top, text="Knife", border=2,font=(20),height= 5, width=20,fg = "white",bg = "blue",command=lambda: [stage1(),select()])
    Knife.place(x=500,y=200)
    Knife.bind("<Enter>",btn_enter3)
    Knife.bind("<Leave>",btn_leave3)
    no3 = Label(top,text=" 3 \n A sharp knife ",font=("Times", 14),bg='#fde5c4')  # FACA2F
    no3.place(x=550,y=350)

    bomb = Button(top, text="Bomb", border=2,font=(20),height= 5, width=20,fg = "white",bg = "red",command=lambda: [stage1(),select()])
    bomb.place(x=500,y=430)
    bomb.bind("<Enter>",btn_enter4)
    bomb.bind("<Leave>",btn_leave4)
    no4 = Label(top,text=" 4 \n A grenade. ",font=("Times", 14),bg='#fde5c4')  # FACA2F
    no4.place(x=550,y=570)
 
 ############## WELCOME TO THE TREASURE #####################
    


top.mainloop()


