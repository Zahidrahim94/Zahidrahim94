from tkinter import *

main_window = Tk()
# label
Label(main_window, text="Enter ypur name ").grid(row=0, column= 0)
Label(main_window, text="What is yor age ").grid(row=1, column= 0)
# textinput
myName =Entry(main_window, width=50, borderwidth=5).grid(row=0,column=1)
myAge =Entry(main_window, width=50, borderwidth=5).grid(row=1,column=1)



# callbackfunction
def on_click():
    print(f"my name is {myName} , and my age is {myAge}" )
    # Button
Button(main_window,text="Click here" , command= on_click).grid(row=5,column=1)

main_window.mainloop()