import tkinter as tk


def check():
    if cval.get() is True:
        print('チェックされています')
    else:
        print('チェックされていません')


root = tk.Tk()
root.title('My Window')
root.geometry('400x200')

cval = tk.BooleanVar()
cval.set(False)
cbtn = tk.Checkbutton(text='チェックボタン', variable=cval, command=check)
cbtn.pack()
root.mainloop()
