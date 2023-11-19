import tkinter as tk # Basic logics
from tkinter import ttk # All the widges
import ttkbootstrap as ttk # Lib for styling

def main():

    def convert():
        mile_input = entry_int.get()
        km_output = mile_input * 1.61
        output_string.set(km_output)

    # basic window settings
    window = ttk.Window(themename='darkly')
    window.title('Demo')
    window.geometry('400x150')

    # widgets
        # title
    title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 24 bold') # window is the container of the widget
    title_label.pack() # in order to appear in the container

        # input field
    input_frame = ttk.Frame(master=window)
    entry_int = tk.IntVar()
    entry = ttk.Entry(master=input_frame, textvariable=entry_int)
    button = ttk.Button(master=input_frame, text='Convert', command=convert)
    entry.pack(side='left', padx=10)    
    button.pack(side='left')   
    input_frame.pack(pady=10)

        # output
    output_string = tk.StringVar()
    output_label = ttk.Label(
        master=window,
        text='Output',
        font='Calibri 24',
        textvariable=output_string
        )
    output_label.pack(pady=5)


    # run
    window.mainloop()   


if __name__ == '__main__':
    main()
