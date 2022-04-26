import tkinter


def left_click_handler(event_object):
    print("Left button clicked")


def double_button_handler(event_object):
    print("button clicked twice")


def main():
    root_window = tkinter.Tk()
    root_window.title("Bind Demo")

    demo_button = tkinter.Button(root_window, padx=10, pady=10)
    demo_button.configure(text="OK")
    demo_button.pack()

    demo_button.bind('<Button-1>', left_click_handler)
    demo_button.bind('<Double-1>', double_button_handler)

    root_window.mainloop()


main()