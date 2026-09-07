import tkinter as tk

score_x = 0
score_o = 0
score = (score_x, "-", score_o)
turn = "X"
slot1_e = "blank"
slot4_e = "blank"
slot7_e = "blank"
slot2_e = "blank"
slot5_e = "blank"
slot8_e = "blank"
slot3_e = "blank"
slot6_e = "blank"
slot9_e = "blank"

window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("500x500")

win = tk.Label(window, text = score, font = ("Arial", 20, "bold"))
win.pack(pady = 10)

def slot1_picked():
    global turn
    global slot1_e
    if slot1_e == "blank":
        slot1.config(text = turn)
        if turn == "X":
            slot1_e = "X"
            turn = "O"
        else:
            slot1_e = "O"
            turn = "X"
    check_win()
            
def slot4_picked():
    global turn
    global slot4_e
    if slot4_e == "blank":
        slot4.config(text = turn)
        if turn == "X":
            slot4_e = "X"
            turn = "O"
        else:
            slot4_e = "O"
            turn = "X"
    check_win()
            
def slot7_picked():
    global turn
    global slot7_e
    if slot7_e == "blank":
        slot7.config(text = turn)
        if turn == "X":
            slot7_e = "X"
            turn = "O"
        else:
            slot7_e = "O"
            turn = "X"
    check_win()
            
def slot2_picked():
    global turn
    global slot2_e
    if slot2_e == "blank":
        slot2.config(text = turn)
        if turn == "X":
            slot2_e = "X"
            turn = "O"
        else:
            slot2_e = "O"
            turn = "X"
    check_win()
            
def slot5_picked():
    global turn
    global slot5_e
    if slot5_e == "blank":
        slot5.config(text = turn)
        if turn == "X":
            slot5_e = "X"
            turn = "O"
        else:
            slot5_e = "O"
            turn = "X"
    check_win()
            
def slot8_picked():
    global turn
    global slot8_e
    if slot8_e == "blank":
        slot8.config(text = turn)
        if turn == "X":
            slot8_e = "X"
            turn = "O"
        else:
            slot8_e = "O"
            turn = "X"
    check_win()
            
def slot3_picked():
    global turn
    global slot3_e
    if slot3_e == "blank":
        slot3.config(text = turn)
        if turn == "X":
            slot3_e = "X"
            turn = "O"
        else:
            slot3_e = "O"
            turn = "X"
    check_win()
            
def slot6_picked():
    global turn
    global slot6_e
    if slot6_e == "blank":
        slot6.config(text = turn)
        if turn == "X":
            slot6_e = "X"
            turn = "O"
        else:
            slot6_e = "O"
            turn = "X"
    check_win()
            
def slot9_picked():
    global turn
    global slot9_e
    if slot9_e == "blank":
        slot9.config(text = turn)
        if turn == "X":
            slot9_e = "X"
            turn = "O"
        else:
            slot9_e = "O"
            turn = "X"
    check_win()

canvas = tk.Canvas(window, width = 480, height = 470, bg = "#80C1FF")
canvas.pack()
canvas.create_line(10, 140, 472, 140, fill = "black", width = 5)
canvas.create_line(10, 300, 472, 300, fill = "black", width = 5)
canvas.create_line(160, 450, 160, 10, fill = "black", width = 5)
canvas.create_line(320, 450, 320, 10, fill = "black", width = 5)

slot1 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"),  
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot1_picked
    )
slot1.pack()
slot1.place(x = 25, y = 60, width = 140, height = 125)

slot4 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"), 
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot4_picked
    )
slot4.pack()
slot4.place(x = 25, y = 200, width = 140, height = 125)

slot7 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"), 
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot7_picked
    )
slot7.pack()
slot7.place(x = 25, y = 360, width = 140, height = 125)

slot2 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"), 
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot2_picked
    )
slot2.pack()
slot2.place(x = 180, y = 60, width = 140, height = 125)

slot5 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"), 
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot5_picked
    )
slot5.pack()
slot5.place(x = 180, y = 200, width = 140, height = 125)

slot8 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"), 
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot8_picked
    )
slot8.pack()
slot8.place(x = 180, y = 360, width = 140, height = 125)

slot3 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"), 
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot3_picked
    )
slot3.pack()
slot3.place(x = 335, y = 60, width = 140, height = 125)

slot6 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"), 
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot6_picked
    )
slot6.pack()
slot6.place(x = 335, y = 200, width = 140, height = 125)

slot9 = tk.Button(
    window, 
    text = "", 
    font = ("Arial", 50, "bold"), 
    bg = "#4DA6FF", 
    fg = "white", 
    activebackground = "#80C1FF", 
    activeforeground = "white", 
    command = slot9_picked
    )
slot9.pack()
slot9.place(x = 335, y = 360, width = 140, height = 125)

def check_win():
    global slot1_e
    global slot2_e
    global slot3_e
    global slot4_e
    global slot5_e
    global slot6_e
    global slot7_e
    global slot8_e
    global score_x
    global score_o
    global slot9_e
    if slot1_e == "X" and slot2_e == "X" and slot3_e == "X":
        score_x = score_x + 1
        reset()
    if slot4_e == "X" and slot5_e == "X" and slot6_e == "X":
        score_x = score_x + 1
        reset()
    if slot7_e == "X" and slot8_e == "X" and slot9_e == "X":
        score_x = score_x + 1
        reset()
    if slot1_e == "X" and slot4_e == "X" and slot7_e == "X":
        score_x = score_x + 1
        reset()
    if slot2_e == "X" and slot5_e == "X" and slot8_e == "X":
        score_x = score_x + 1
        reset()
    if slot3_e == "X" and slot6_e == "X" and slot9_e == "X":
        score_x = score_x + 1
        reset()
    if slot1_e == "X" and slot5_e == "X" and slot9_e == "X":
        score_x = score_x + 1
        reset()
    if slot3_e == "X" and slot5_e == "X" and slot7_e == "X":
        score_x = score_x + 1
        reset()
    if slot1_e == "O" and slot2_e == "O" and slot3_e == "O":
        score_o = score_o + 1
        reset()
    if slot4_e == "O" and slot5_e == "O" and slot6_e == "O":
        score_o = score_o + 1
        reset()
    if slot7_e == "O" and slot8_e == "O" and slot9_e == "O":
        score_o = score_o + 1
        reset()
    if slot1_e == "O" and slot4_e == "O" and slot7_e == "O":
        score_o = score_o + 1
        reset()
    if slot2_e == "O" and slot5_e == "O" and slot8_e == "O":
        score_o = score_o + 1
        reset()
    if slot3_e == "O" and slot6_e == "O" and slot9_e == "O":
        score_o = score_o + 1
        reset()
    if slot1_e == "O" and slot5_e == "O" and slot9_e == "O":
        score_o = score_o + 1
        reset()
    if slot3_e == "O" and slot5_e == "O" and slot7_e == "O":
        score_o = score_o + 1
        reset()
    if slot1_e != "blank" and slot2_e != "blank" and slot3_e != "blank" and slot4_e != "blank" and slot5_e != "blank" and slot6_e != "blank" and slot7_e != "blank" and slot8_e != "blank" and slot9_e != "blank":
        score_x = score_x + 0.5
        score_o = score_o + 0.5
        reset()
        
def reset():
    global slot1_e
    global slot2_e
    global slot3_e
    global slot4_e
    global slot5_e
    global slot6_e
    global slot7_e
    global slot8_e
    global slot9_e
    global turn
    global score
    global score_x
    global score_o
    slot1_e = "blank"
    slot2_e = "blank"
    slot3_e = "blank"
    slot4_e = "blank"
    slot5_e = "blank"
    slot6_e = "blank"
    slot7_e = "blank"
    slot8_e = "blank"
    slot9_e = "blank"
    turn = "X"
    score = (score_x, "-", score_o)
    win.config(text = score)
    slot1.config(text = "")
    slot2.config(text = "")
    slot3.config(text = "")
    slot4.config(text = "")
    slot5.config(text = "")
    slot6.config(text = "")
    slot7.config(text = "")
    slot8.config(text = "")
    slot9.config(text = "")
    
window.mainloop()
