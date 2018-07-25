# Name Address | Created by Kyle Daniels @ Southwestern Illinois College

import tkinter

class ShowInfoGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame, textvariable = self.value)
        self.address_button = tkinter.Button(self.bottom_frame, text = "Show Info", command = self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
        self.address_label.pack()
        self.address_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def show_info(self):
        self.value.set("Southwestern Illinois College\n" +
                       "2500 Carlyle Ave.\n" +
                       "Belleville, IL  62220")

show_info = ShowInfoGUI()
        
