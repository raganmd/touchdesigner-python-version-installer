import tkinter as tk

window = tk.Tk()
window.geometry('350x200') 
window.title("Welcome to LikeGeeks app")

lbl = tk.Label(window, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked")

btn = tk.Button(window, text="Click Here", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()

