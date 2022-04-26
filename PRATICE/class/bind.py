from tkinter import *
from sys import *


def showpos(event):
    print("co-ordinates of widget %s on label are: \n x is %s \n y is %s" % (event.widget, event.x, event.y))


def showall(event):
    print("type(event):", type(event))
    for attr in dir(event):
        if not attr.startswith('__'):
            getattr(event, attr)


def middleclick(event):
    print("middle button is clicked")
    showpos(event)


def leftclick(event):
    print("left button is pressed")
    showpos(event)


def rightclick(event):
    print("right button is clicked")
    showpos(event)


def leftdoubleclick(event):
    print("double clicked left button")
    showpos(event)


def main():
    root_window = Tk()
    root_window.title("Bind Program for all mouse & keyboard events")

    widget = Button(root_window)
    label_font = ('courier', 20, 'bold')
    widget.configure(text="Bind Demo Button", bg='green', font=label_font)
    widget.pack(side=TOP)

    widget.bind('<Button-1>', leftclick)
    widget.bind('<Button-2>', middleclick)
    widget.bind('<Button-3>', rightclick)
    widget.bind('<Double-1>', leftdoubleclick)
    widget.bind('<Double-3>', rightdoubleclick)

    widget.focus()

    root_window.mainloop()


main()



