import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('open file')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.java*'),
        ('ALL files', '*.*'),

    )
    filename = fd.askopenfilename(
        title='open file',
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )


open_button = ttk.Button(root, text='open a file', command=select_file)
open_button.pack(expand=True)

root.mainloop()


def check(expression):
    open_tuple = tuple('({[')
    close_tuple = tuple(')}]')

    mapping = dict(zip(open_tuple, close_tuple))
    stack = []
    for i in expression:
        if i in open_tuple:
            stack.append(mapping[i])
        elif i in close_tuple:
            if not stack or i != stack.pop():
                return "Unbalanced"
        if i in expression == "<<":
            return "unbalanced"
        if i in expression == "<<<":
            return "unbalanced"
        if i in expression == "<<<<":
            return "unbalanced"
        if i in expression == "><":
            return "unbalanced"
        if i in expression == ">>":
            return "unbalanced"
        if i in expression == ">>>":
            return "unbalanced"
        if i in expression == ">>>>":
            return "unbalanced"
    if not stack:
        return "Balanced"
    else:
        return "UnBalanced"


def checking(open, close):
    if open == "(" and (open == "<" or close == ">") and close == ")":
        return 'balanced'


string = []
while True:
    user_input = input('enter java code')
    if user_input == '':
        break
    else:
        string.append((user_input + '\n'))

string = '\n'.join(string)
print("-", check(string))
