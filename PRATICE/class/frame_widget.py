import tkinter
import sys


def main():
    root_window = tkinter.Tk()
    root_window.title("Demo for frame widget using Anchor")

    master_frame = tkinter.Frame(root_window)

    frame1 = tkinter.Frame(master_frame)
    frame1.pack(side=tkinter.TOP, anchor=tkinter.N)

    button1 = tkinter.Button(frame1)
    button1.configure(text="TOP-LEFT", command=sys.exit)
    button1.pack(side=tkinter.LEFT, expand=tkinter.YES, anchor=tkinter.E)

    button2 = tkinter.Button(frame1)
    button2.configure(text="TOP-RIGHT", command=sys.exit)
    button2.pack(side=tkinter.LEFT, expand=tkinter.YES, anchor=tkinter.W)

    frame2 = tkinter.Frame(master_frame)
    frame2.pack(side=tkinter.TOP, anchor=tkinter.N)

    button3 = tkinter.Button(frame2)
    button3.configure(text="BOTTOM-LEFT", command=sys.exit)
    button3.pack(side=tkinter.LEFT, expand=tkinter.YES, anchor=tkinter.E)

    button4 = tkinter.Button(frame2)
    button4.configure(text="BOTTOM-RIGHT", command=sys.exit)
    button4.pack(side=tkinter.LEFT, expand=tkinter.YES, anchor=tkinter.W)

    master_frame.pack(side=tkinter.TOP, expand=tkinter.YES)
    root_window.mainloop()

main()
