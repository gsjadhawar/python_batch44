import tkinter


def my_handler():
    print("Button is clicked")


def main():
    root_window = tkinter.Tk()
    root_window.title("Practicing GUI Programming")
    button_widget = tkinter.Button(root_window)

    button_widget.configure(text="PRESS", command=my_handler)

    button_widget.pack(side=tkinter.LEFT, expand=tkinter.YES)

    root_window.mainloop()


main()
