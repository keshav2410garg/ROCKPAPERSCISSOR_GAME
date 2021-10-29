import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from tkinter import messagebox
from tkinter import*

gui=Tk()
gui.config(bg='red')
gui.title("USER MANUAL")
gui.geometry('300x300')
a=Label(gui,text="**GAME INSTRUCTIONS** 📃",fg ="yellow",bg="black")
b= Label(gui, text = "1. START GAME - BEGINS THE FIGHT!! 👿 ", fg ="yellow",bg="black")
c=Label(gui, text = "2. SPACE BAR - DECLARES THE WINNER!! 👑",fg ="yellow",bg="black")
d=Label(gui, text = "3. DOUBLE PRESS Q - NEXT ROUND!! 🔁",fg="yellow",bg="black")
btn=Button(gui, text = "BEGIN 🏁" ,fg = "white",bg="black")
btn.grid(row=1, column=3, padx=(2, 35))
a.grid(row=2, column=3, padx=(2, 35))
b.grid(row=3, column=3, padx=(2, 35))
c.grid(row=4, column=3, padx=(2, 35))
d.grid(row=5, column=3, padx=(2, 35))
gui.mainloop()