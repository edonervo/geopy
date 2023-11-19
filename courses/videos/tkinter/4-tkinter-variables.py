import tkinter as tk
from tkinter import ttk 

def main():

    def button_func():
        print(string_var.get())
        string_var.set('button_pressed')

    window = tk.Tk()
    window.title('Tkinter Variables')

    # tkinter variables
    string_var = tk.StringVar()

    # widgets
    label = ttk.Label(master=window, text='label', textvariable=string_var)
    entry = ttk.Entry(master=window, textvariable=string_var)
    label.pack()
    entry.pack()

    button = ttk.Button(master=window, text='button', command=button_func)
    button.pack()

    # exercise
    ex_str_var = tk.StringVar(value='test')
    ex_label = ttk.Label(master=window, text='label', textvariable=ex_str_var)
    ex_entry_1 = ttk.Entry(master=window, textvariable=ex_str_var)
    ex_entry_2 = ttk.Entry(master=window, textvariable=ex_str_var)

    ex_label.pack()
    ex_entry_1.pack()
    ex_entry_2.pack()

    # mainloop
    window.mainloop()

if __name__:
    main()