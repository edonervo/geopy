import tkinter as tk
from tkinter import ttk

def main():

    def button_func():
        entry_text = entry.get()
        # Update the label - Two possibilities
        # label.configure(text='Some Other Text')
        # label['text'] = 'Some Other Text' # |Better|
        label['text'] = entry_text
        entry['state'] = 'disabled'
        # print(label.configure()) # Gets all the possible configuration
    
    def other_button_func():
        label['text'] = 'some text'
        entry['state'] = 'enabled'


    window = tk.Tk()
    window.title('Getting and setting widgetts')

    # widgets
    label = ttk.Label(master=window, text='My Label')
    entry = ttk.Entry(master=window)
    button = ttk.Button(master=window, text='My Button', command=button_func)
    label.pack()
    entry.pack()
    button.pack()

    # New button
    other_button = ttk.Button(master=window, text='another button', command=other_button_func)

    other_button.pack()

    window.mainloop()

if __name__ == '__main__':
    main()


