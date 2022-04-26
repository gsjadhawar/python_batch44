import tkinter, sys

def main():
    root_window = tkinter.Tk()
    root_window.title("demo for top level - this is root window")

    widget_label = tkinter.Button(root_window)
    widget_label.configure(text="OK", command=sys.exit)
    widget_label.pack()

    tp_win1 = tkinter.Toplevel()
    tp_win2 = tkinter.Toplevel()

    tp_win1.protocol("WM_DELETE_WINDOW", lambda: None)
    tp_win2.protocol("WM_DELETE_WINDOW", lambda: None)

    button_1 = tkinter.Button(tp_win1)
    button_1.configure(text="button_1-pop1", command=tp_win1.destroy)
    button_1.pack()

    button_2 = tkinter.Button(tp_win2)
    button_2.configure(text="button_2-pop2", command=tp_win2.destroy)
    button_2.pack()

    root_window.mainloop()


main()


