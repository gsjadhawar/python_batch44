import tkinter
import time


def time_handler():
    time_stamp = time.time()
    handler(time_stamp)


def handler(time_stamp):
    print(time.ctime(time_stamp))


def main():
    root_window = tkinter.Tk()
    root_window.title("Demo for handler with parameter argument")

    button_widget = tkinter.Button(root_window)

    button_widget.configure(text="ok", command=time_handler)

    button_widget.pack()

    button_widget.mainloop()

main()
