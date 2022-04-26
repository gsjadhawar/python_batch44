import tkinter


def main():
    root_window = tkinter.Tk()
    root_window.title("Title - GUI Programming Practice")

    label_widget = tkinter.Label(root_window)
    label_widget.configure(text="This is written in client area")
    label_widget.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.X)

    root_window.mainloop()

main()

