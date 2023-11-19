import tkinter as tk
from tkinter import ttk

def main():

    def button_func():
        print('A button was pressed')

    def other_button_func():
        print('Hello!')

    # Create a window
    window = tk.Tk()
    window.title('Windows and Widgets')
    window.geometry('800x700')

    # ttk widgets
    label = ttk.Label(master=window, text='This is a test')
    label.pack()

    # Create Widgets (tk)
    text = tk.Text(master=window)
    text.pack() # Text Box

    ## ttk entry
    entry = ttk.Entry(master=window)
    entry.pack()

    ## ttk button
    other_label = ttk.Label(master=window, text='My Label')
    other_label.pack()
    button = ttk.Button(master=window, text='A Button', command=button_func)
    button.pack()

    ## other button and label
    # other_button = ttk.Button(master=window, text='Other button', command=other_button_func)
    other_button = ttk.Button(master=window, text='Other button', command=lambda: print('hello'))
    other_button.pack()

    # run
    window.mainloop()

if __name__ == '__main__':
    main()