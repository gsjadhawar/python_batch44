import sys
import tkinter
import time


def time_handler():
    time_stamp = time.time()
    handler(time_stamp)


def handler(time_stamp):
    print(time.ctime(time_stamp))


def platform_handler():
    print(sys.platform)


def main():
    root_window = tkinter.Tk()
    root_window.title("Demo for handler with parameter argument")

    button_widget = tkinter.Button(root_window)
    button_widget.configure(text="time", command=time_handler)
    button_widget.pack(side=tkinter.TOP, expand=tkinter.NO)

    button_widget_2 = tkinter.Button(root_window)
    button_widget_2.configure(text="platform", command=platform_handler)
    button_widget_2.pack(side=tkinter.TOP, expand=tkinter.NO)

    button_widget_3 = tkinter.Button(root_window)
    button_widget_3.configure(text="exit", command=sys.exit)
    button_widget_3.pack(side=tkinter.TOP, expand=tkinter.NO)

    root_window.mainloop()

main()
