import tkinter as tk

def press(num):
    entry_text.set(entry_text.get() + str(num))

def equalpress():
    try:
        total = str(eval(entry_text.get()))
        entry_text.set(total)
    except:
        entry_text.set("Error")

def clear():
    entry_text.set("")

root = tk.Tk()
root.title("Realistic Calculator")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#222222")

entry_text = tk.StringVar()

entry = tk.Entry(root, font=('Arial', 20), textvariable=entry_text, bd=10, insertwidth=2,
                 width=14, borderwidth=4, relief='ridge', bg="#e0e0e0", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  bg="#4caf50", fg="white", command=equalpress).grid(row=row, column=col, columnspan=1, sticky="nsew")
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  bg="#f44336", fg="white", command=clear).grid(row=row, column=col, columnspan=4, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                  bg="#333333", fg="white", command=lambda t=text: press(t)).grid(row=row, column=col)

root.mainloop()
