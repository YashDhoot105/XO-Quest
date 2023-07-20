from tkinter import*
import random


def next_turn(row , column):

    global Player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if Player == Players[0]:

            buttons[row][column]['text'] = Player

            if check_winner() is False:

                Player = Players[1]
                label.config(text=Players[1] +"'s  Turn")

            elif check_winner() is True:

                label.config(text=Players[0] +"  wins the game :)")

            elif check_winner() == "Tie":

                label.config(text="Tie !!")

        else:

            buttons[row][column]['text'] = Player

            if check_winner() is False:

                Player = Players[0]
                label.config(text=Players[0] +"'s  Turn")

            elif check_winner() is True:

                label.config(text=Players[1] +"  wins the game :)")

            elif check_winner() == "Tie":

                label.config(text="Tie !!")


def empty_spaces():

    spaces = 9

    for row in range(3):

        for column in range (3):

            if buttons[row][column]['text'] != "":

                spaces-=1

    if spaces == 0:

        return False

    else:

        return True

    
def check_winner():

    for column in range(3):

        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":

            buttons[0][column].config(bg='#b4bbc3')
            buttons[1][column].config(bg='#b4bbc3')
            buttons[2][column].config(bg='#b4bbc3')
            return True
        
    for row in range (3):

        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":

            buttons[row][0].config(bg='#b4bbc3')
            buttons[row][1].config(bg='#b4bbc3')
            buttons[row][2].config(bg='#b4bbc3')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":

        buttons[0][0].config(bg='#b4bbc3')
        buttons[1][1].config(bg='#b4bbc3')
        buttons[2][2].config(bg='#b4bbc3')
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":

        buttons[0][2].config(bg='#b4bbc3')
        buttons[1][1].config(bg='#b4bbc3')
        buttons[2][0].config(bg='#b4bbc3')
        return True
    
    elif empty_spaces()is False:

        for row in range(3):

            for column in range (3):

                buttons[row][column].config(bg= "#b4bbc3") 

        return "Tie"
        
    else:

        return False


def new_game():

    global Player

    Player = random.choice(Players)
    label.config( text=Player +"'s  Turn" )

    for row in range(3):

        for column in range (3):

             buttons[row][column].config(text= "" , bg="#1B2223")



window = Tk()
window.configure(bg="#0EF6CC")
window.title("Tic-Tac-Toe")
Players = ["x" , "o"]
Player = random.choice(Players)
buttons = [[0,0,0] , 
           [0,0,0] ,
           [0,0,0]]


label = Label(window , text=Player +"'s  Turn" , font=('Comic Sans Ms' , 40), background="#0EF6CC" , fg = '#3A4F50' )
label.pack(side="top")

reset_button = Button(window , text="Restart" ,fg = '#fff' , activebackground='#b4bbc3' ,background='grey' ,activeforeground="#fff" , font=('Comic Sans Ms' , 20) , relief='groove' , pady=5 , command=new_game)
reset_button.pack(side="top")

frame = Frame(window , bg="pink")
frame.pack()


for row in range(3):

    for column in range(3):
        
        buttons[row][column] = Button(frame , text= "" , font=('Comic Sans Ms' , 40) , bg="#1B2223",fg="#F4FEFD", activeforeground="#3A4F50", width = 5 , height = 2 , command=lambda row=row , column= column: next_turn(row , column))
        buttons[row][column].grid(row=row , column=column )

window.mainloop()