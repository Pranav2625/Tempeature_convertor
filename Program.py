# 01_Help_GUI.py
from logging import root
# from functools import partial # To prevent unwanted windows
from tkinter import *
import random


class Converter:
    def __init__(self, parent):
        
        # Formatting Variables:
        # window_colour = "light blue"
        window_colour = 'Maroon'
        main_txt_box_clr = 'Gold'

        # Converter Main Screen UI:
        self.converter_frame = Frame(width = 700, height = 400, bg=window_colour) # Determines dimensions and colour of frame/window
        self.converter_frame.grid() 

        # Converter Heading (row 0):
        self.converter_label = Label(text = 'Temperature Converter', font = ("Arial", "16", 'bold'),
        bg = main_txt_box_clr, 
        padx = 10, pady = 10)
        self.converter_label.grid(row = 0)



# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()