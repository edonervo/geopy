import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()
    window.title('buttons')
    window.geometry('600x400')

    # button
    def button_func():
        print('a basic button')
    button_string = tk.StringVar(value='A button with string var')
    button = ttk.Button(window, text='A simple Button', command=button_func, textvariable=button_string)
    button.pack()

    # check button
    check_var = tk.IntVar()
    check1 = ttk.Checkbutton(
        window, 
        text='checkbox 1',
        command=lambda: print(check_var.get()),
        variable=check_var,
        onvalue=10,
        offvalue=5
        )
    check2 = ttk.Checkbutton(
        window, 
        text='checkbox 2',
        command=lambda: print(check_var.set(5)) 
        )
    check1.pack()
    check2.pack()

    # Radio buttons
    radio_var = tk.StringVar()
    radio1 = ttk.Radiobutton(
        window,
        text='Radiobutton 1',
        value='radio1',
        variable=radio_var,
        command=lambda: print(radio_var.get()),
        )
    radio2 = ttk.Radiobutton(
        window,
        text='Radiobutton 2',
        value=2,
        variable=radio_var,
        command=lambda: print(radio_var.get()),
        )
    
    radio1.pack()
    radio2.pack()

    # exercise radio button
    radio_ex_var = tk.StringVar()
    def radio_ex_func():
        print(is_checked.get())
        is_checked.set(False)

    radio_ex_1 = ttk.Radiobutton(
        master=window,
        text='Ex RadioButton A',
        value='A',
        variable=radio_ex_var,
        command=radio_ex_func
    )
    radio_ex_2 = ttk.Radiobutton(
        master=window,
        text='Ex RadioButton B',
        value = 'B',
        command=radio_ex_func,
        variable=radio_ex_var
    )
    radio_ex_1.pack()
    radio_ex_2.pack()

    # exercise check button
    def check_ex_func():
        print('Radio button value:' + radio_ex_var.get())

    is_checked = tk.BooleanVar(value=True)
    check_ex = ttk.Checkbutton(
        master=window,
        text='Exercise Button',
        variable=is_checked,
        onvalue=True,
        offvalue=False,
        command=check_ex_func
        )
    check_ex.pack()



    # run
    window.mainloop()


if __name__ == '__main__':
    main()