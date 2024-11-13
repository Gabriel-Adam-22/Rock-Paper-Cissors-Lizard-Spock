from tkinter import *
from random import *
from os import *

root = Tk()
root.title("Pierre Feuille Ciseau Lezard Spock")
root.geometry("680x500")
root.config(bg="#ffae00")

title = Label(root,text="Faites votre choix :",font=("Terminal",12))
title.config(bg="#ffae00",pady=15)
title.place(x=0,y=0)

space=Label(root,text="\n\n")
space.config(bg="#ffae00")
space.grid(row=0,column=3)


global Selected_item,User
Selected_item=""
User=""


def Rock_F(e):
    global Selected_item,User
    Selected_item = "Pierre"
    User = PhotoImage(file="PFC_picts\\Pierre.png")

def Paper_F(e):
    global Selected_item,User
    Selected_item = "Papier"
    User = PhotoImage(file="PFC_picts\\Feuille.png")

def Cissors_F(e):
    global Selected_item,User
    Selected_item = "Ciseau"
    User = PhotoImage(file="PFC_picts\\Ciseau.png")

def Lizard_F(e):
    global Selected_item,User
    Selected_item = "Lezard"
    User = PhotoImage(file="PFC_picts\\Lezard.png")

def Spock_F(e):
    global Selected_item,User
    Selected_item = "Spock"
    User = PhotoImage(file="PFC_picts\\Spock.png")


## Pierre
    # Button
pierre_img = PhotoImage(file="PFC_picts\\Pierre.png")
Pierre_button = Label(image=pierre_img,bg="#ffae00")
Pierre_button.bind("<Button-1>",Rock_F)
Pierre_button.grid(row=1,column=0,padx=15)
    # Label
pierre_label= Label(root,text="Pierre",font=("Terminal",12))
pierre_label.config(bg="#ffae00")
pierre_label.grid(row=2,column=0)



##Feuille
    # Button
feuille_img = PhotoImage(file="PFC_picts\\Feuille.png")
Feuille_button = Label(image=feuille_img,bg="#ffae00")
Feuille_button.bind("<Button-1>",Paper_F)
Feuille_button.grid(row=1,column=1)
    # Label
feuille_label= Label(root,text="Feuille",font=("Terminal",12))
feuille_label.config(bg="#ffae00")
feuille_label.grid(row=2,column=1)

##Ciseau
    # Button
ciseau_img = PhotoImage(file="PFC_picts\\Ciseau.png")
ciseau_button = Label(image=ciseau_img,bg="#ffae00")
ciseau_button.bind("<Button-1>", Cissors_F)
ciseau_button.grid(row=1,column=2,padx=15)
    # Label
ciseau_label= Label(root,text="Ciseau",font=("Terminal",12))
ciseau_label.config(bg="#ffae00")
ciseau_label.grid(row=2,column=2)

##Lezard
    # Button
lezard_img = PhotoImage(file="PFC_picts\\Lezard.png")
Lezard_button = Label(image=lezard_img,bg="#ffae00")
Lezard_button.bind("<Button-1>",Lizard_F)
Lezard_button.grid(row=1,column=3)
    # Label
lezard_label= Label(root,text="Lezard",font=("Terminal",12))
lezard_label.config(bg="#ffae00")
lezard_label.grid(row=2,column=3)

##Spock
    # Button
spock_img = PhotoImage(file="PFC_picts\\Spock.png")
Spock_button = Label(image=spock_img,bg="#ffae00")
Spock_button.bind("<Button-1>",Spock_F)
Spock_button.grid(row=1,column=4,padx=15)
    # Label
spock_label= Label(root,text="Spock",font=("Terminal",12))
spock_label.config(bg="#ffae00")
spock_label.grid(row=2,column=4)



Pc_choice = randint(1,5)
    
Pc=""
if Pc_choice == 1:
    Pc = PhotoImage(file="PFC_picts\\Pierre.png")
elif Pc_choice == 2:
    Pc = PhotoImage(file="PFC_picts\\Feuille.png")
elif Pc_choice == 3:
    Pc = PhotoImage(file="PFC_picts\\Ciseau.png")
elif Pc_choice == 4:
    Pc = PhotoImage(file="PFC_picts\\Lezard.png")
elif Pc_choice == 5:
    Pc = PhotoImage(file="PFC_picts\\Spock.png")


def v(e):
    if Selected_item.strip(" ") != "":
        print(Selected_item)

        title.destroy()
        
        Pierre_button.destroy()
        pierre_label.destroy()

        Feuille_button.destroy()
        feuille_label.destroy()

        ciseau_button.destroy()
        ciseau_label.destroy()

        Lezard_button.destroy()
        lezard_label.destroy()

        Spock_button.destroy()
        spock_label.destroy()

        vb.destroy()


        
        User_Label = Label(image=User)
        User_Label.grid(row=1,column=1,padx=100)

        Vs_label = Label(root,text="Vs",bg="#ffae00",font=("Terminal",15))
        Vs_label.grid(row=1,column=2)


        Pc_Label = Label(image=Pc)
        Pc_Label.grid(row=1,column=3,padx=100)

        if Pc_choice == 1:
            if Selected_item == "Pierre":
                Result=Label(root,text="Egalitée",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=65)
            elif Selected_item == "Papier":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Lezard":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Spock":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Ciseau":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)

        elif Pc_choice == 2:
            if Selected_item == "Pierre":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Papier":
                Result=Label(root,text="Egalitée",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=65)
            elif Selected_item == "Lezard":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Spock":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Ciseau":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)

        elif Pc_choice == 3:
            if Selected_item == "Pierre":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Papier":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Lezard":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Spock":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Ciseau":
                Result=Label(root,text="Egalitée",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=65)

        elif Pc_choice == 4:
            if Selected_item == "Pierre":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Papier":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Lezard":
                Result=Label(root,text="Egalitée",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=65)
            elif Selected_item == "Spock":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Ciseau":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)

        elif Pc_choice == 5:
            if Selected_item == "Pierre":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Papier":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Lezard":
                Result=Label(root,text="Gagné",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)
            elif Selected_item == "Spock":
                Result=Label(root,text="Egalitée",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=65)
            elif Selected_item == "Ciseau":
                Result=Label(root,text="Perdu",bg="#ffae00",font=("Elephant",12))
                Result.grid(row=2,column=2,pady=15)


vb_img = PhotoImage(file="PFC_picts\\Done4.png")
vb = Label(image=vb_img)
vb.bind("<Button-1>",v)
vb.config(bg="#ffae00")
vb.grid(row=3,column=2,pady=40)

root.mainloop()