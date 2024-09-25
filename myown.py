from tkinter import *
from tkinter import ttk

class SayHello:

    def __init__(self, root):
        root.title('Hello')

        mainframe = ttk.Frame(root, padding='12 12 12 12')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.name = StringVar()
        name_entry = ttk.Entry(mainframe, width=8, textvariable=self.name)
        name_entry.grid(column=1, row=2, sticky=(N, W))
        self.hello = StringVar()

        ttk.Label(mainframe, textvariable=self.hello).grid(column=1, row=1, sticky=(E, S))
        ttk.Button(mainframe, text='Hello', command=self.Hi).grid(column=3, row=3, sticky=(N))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)


        name_entry.focus()
        root.bind('<Return>', self.Hi)

    def Hi(self, *args):
        try:
            value = float(self.hello.get())
            self.hello.set(f'Hello {self.hello}')
        except ValueError:
            pass

root = Tk()
SayHello(root)
root.mainloop()