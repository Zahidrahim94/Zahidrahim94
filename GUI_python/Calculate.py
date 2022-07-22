from tkinter import *
main_window = Tk()
# label
Entry(main_window, width=50, borderwidth=5, background="lightblue",).grid(row=0,column=0)
Label(main_window, text="1", width=1, borderwidth=5, background="pink").grid(row=1, column=0)
Label(main_window, text="2", width=1, borderwidth=5, background="pink").grid(row=1, column=1)
Label(main_window, text="3", width=1, borderwidth=5, background="pink").grid(row=1, column=2)
Label(main_window, text="4", width=1, borderwidth=5, background="pink").grid(row=2, column=0)
Label(main_window, text="5",  width=1,borderwidth=5, background="pink").grid(row=2, column=1)
Label(main_window, text="6", width=1, borderwidth=5, background="pink").grid(row=2, column=2)
Label(main_window, text="7",  width=1,borderwidth=5, background="pink").grid(row=3, column=0)
Label(main_window, text="8",  width=1,borderwidth=5, background="pink").grid(row=3, column=1)
Label(main_window, text="9",  width=1,borderwidth=5, background="pink").grid(row=3, column=2)
Label(main_window, text="+",  width=1,borderwidth=5, background="pink").grid(row=4, column=0)
Label(main_window, text="0",  width=1,borderwidth=5, background="pink").grid(row=4, column=1)
Label(main_window, text="-", width=1, borderwidth=5, background="pink").grid(row=4, column=2)
# textinput

# callbackfunction)
# Button
main_window.mainloop()