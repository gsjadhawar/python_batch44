import tkinter
import sys


def main():
    root_window = tkinter.Tk()
    root_window.title("custom button demo")

    custom_button = tkinter.Button(root_window, padx=10, pady=10)
    custom_button.configure(text="ok", command=sys.exit, fg='black', bg='red', bd=10, relief=tkinter.RAISED,
                            font=("helvetica", 20, 'underline italic'), cursor='hand2')
    custom_button.pack(side=tkinter.TOP, expand=tkinter.YES)
    root_window.mainloop()


main()
