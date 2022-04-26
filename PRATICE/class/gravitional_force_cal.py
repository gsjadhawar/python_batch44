from tkinter import *

first = True
global_output_label = None

def compute():
    m1 = float(text_box_string_1.get())
    m2 = float(text_box_string_2.get())
    r = float(text_box_string_3.get())
    G = 6.674 * (10 ** -11)
    F = (G * m1 * m2)/(r**2)
    global first, s, global_output_label, output_label
    s = "gravitional force between m1 & m2 is: %.2f" % F
    if first == True:
        first = False
    else:
        global_output_label.destroy()
    output_label = Label(root_window)
    output_label.configure(text=s)
    output_label.grid(row=5, column=2, sticky=W)
    global_output_label = output_label


def main():
    global text_box_string_1, root_window
    global text_box_string_2
    global text_box_string_3
    global text_box_string_5

    root_window = Tk()
    root_window.title("Gravitational force calculation between two objects")

    L1 = Label(root_window)
    L1.configure(text="Enter Mass of Object1")

    L2 = Label(root_window)
    L2.configure(text="Enter Mass of Object2")

    L3 = Label(root_window)
    L3.configure(text="Enter distance between objects")

    L4 = Label(root_window)
    L4.configure(text="Compute Gravitional Force")

    button1 = Button(root_window)
    button1.configure(text="Compute", command=compute)

    text_box_string_1 = StringVar()
    B1 = Entry(root_window, textvariable=text_box_string_1)

    text_box_string_2 = StringVar()
    B2 = Entry(root_window, textvariable=text_box_string_2)

    text_box_string_3 = StringVar()
    B3 = Entry(root_window, textvariable=text_box_string_3)

    text_box_string_5 = StringVar()
    B5 = Entry(root_window, textvariable=text_box_string_5)

    L1.grid(row=1, column=1, sticky=W)
    L2.grid(row=2, column=1, sticky=W)
    L3.grid(row=3, column=1, sticky=W)
    L4.grid(row=4, column=1, sticky=W)
    B1.grid(row=1, column=2, sticky=W)
    B2.grid(row=2, column=2, sticky=W)
    B3.grid(row=3, column=2, sticky=W)
    button1.grid(row=4, column=2, sticky=W)

    root_window.mainloop()
    compute()

main()