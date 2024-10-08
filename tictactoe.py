import tkinter as tk

def set_tile(row,column):
    global actual

    if (game_over):
        return

    if tablou[row][column]["text"] != "":
        return

    tablou[row][column]["text"] = actual
    if actual == player2:
        actual = player1
    else:
        actual = player2
    label["text"] = actual + "'s turn"

    winner()

def winner():
    global turn, game_over
    turn += 1
    #orizontala
    for row in range(3):
        if (tablou[row][0]["text"] == tablou[row][1]["text"] == tablou[row][2]["text"] and tablou[row][0]["text"] != ""):
            label.config(text=tablou[row][0]["text"]+"is the winner",fg=galben)
            for column in range(3):
                tablou[row][column].config(fg = galben, bg = light_gray)
            game_over = True
            return
    #verticala
    for column in range(3):
        if (tablou[0][column]["text"] == tablou[1][column]["text"] == tablou[2][column]["text"] and tablou[0][column]["text"] != ""):
            label.config(text = tablou[0][column]["text"] + "is the winner!", foreground=galben)
            for row in range(3):
                tablou[row][column].config(foreground=galben, background=light_gray)
            game_over = True
            return
    #diagonala principala    
    if (tablou[0][0]["text"]==tablou[1][1]["text"]==tablou[2][2]["text"] and tablou[0][0]["text"] != ""):
        label.config(text=tablou[0][0]["text"] + "is the winner!", foreground=galben)
        for i in range(3):
            tablou[i][i].config(foreground=galben, background=light_gray)
        game_over = True
    #diagonala secundara
    if (tablou[0][2]["text"]==tablou[1][1]["text"]==tablou[2][0]["text"] and tablou[0][2]["text"] != ""):
            tablou[0][2].config(foreground=galben,background=light_gray)
            tablou[1][1].config(foreground=galben,background=light_gray)
            tablou[2][0].config(foreground=galben,background=light_gray)
    #tie
    if(turn==9):
        game_over = True
        label.config(text = "Tie!", foreground = galben)

def New_Game():
    global turn, game_over
    turn = 0
    game_over = False

    label.config(text = actual + "'s turn", foreground = "white")

    for row in range(3):
        for column in range(3):
            tablou[row][column].config(text = "", foreground = albastru, background = gri)


player1 = "X"
player2 = "O"
actual = player1
tablou = [[0,0,0],
         [0,0,0],
         [0,0,0]]
albastru="#4584b6"
galben="#ffde57"
gri="#343434"
light_gray="#646464"

turn = 0
game_over = False

chenar = tk.Tk()
chenar.title("Tic_Tac_Toe")
chenar.resizable(False,False)

frame = tk.Frame(chenar)
label = tk.Label(frame, text = actual + "'s turn", font = ("Arial",20), bg = gri,fg = "white")

label.grid(row = 0, column = 0, columnspan = 3, sticky = "we")

for row in range(3):
    for column in range(3):
        tablou[row][column] = tk.Button(frame, text = "", font = ("Arial",50,"bold"), bg = gri, fg = albastru, width = 4, height = 1, command = lambda row = row, column = column: set_tile(row, column))
        tablou[row][column].grid(row = row + 1, column = column)

button=tk.Button(frame, text = "restart", font = ("Arial",20), bg = gri, fg = "white", command = New_Game)
button.grid(row = 4, column = 0, columnspan = 3, sticky = "we")

frame.pack()

chenar.update()

chenar.mainloop()