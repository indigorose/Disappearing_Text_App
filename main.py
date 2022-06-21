from tkinter import *
from threading import Timer


window = Tk()
window.geometry("450x350")
timeout = 10


# clear the output and refresh the input
def clear_text():
    input_txt.delete(1.0, END)


# Timer mechanism
def countdown(e):
    count_time = Timer(timeout+10, clear_text)
    count_time.start()


def timer_reset(e):
    pass


# Create a Text Field
title = Label(text="Disappearing Text App")
f1 = Frame(window, background="white", height=5, width=30)
input_txt = Text(window, height=8, width=60, bg="#FFEEEE")
input_txt.tag_configure("center", justify="center")
input_txt.tag_add("center", "1.0", "end")


# Tkinter pack
title.pack()
input_txt.pack()
f1.pack()
window.bind('<KeyRelease>', countdown)

window.mainloop()
