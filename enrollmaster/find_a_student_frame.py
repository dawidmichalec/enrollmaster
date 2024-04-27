from tkinter import *
import ttkbootstrap as ttk


class FindAStudentFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        print("Initialized")
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        frame_label = ttk.Label(self, text='WYSZUKAJ UCZNIA', font=('Open Sans', 14, 'bold'), bootstyle='default')
        frame_label.grid(row=0, column=3, sticky='w')
