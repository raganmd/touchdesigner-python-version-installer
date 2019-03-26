import tkinter as tk
import tkinter.filedialog

window = tk.Tk()
window.geometry('1000x200') 
window.title("TouchDesigner Mulit-Version Manager")

header_font = ("Arial Bold", 20)
dialogue_font = ("Arial", 12)

install_header = tk.Label(window, text="Installs", font=header_font)
install_header.grid(column=0, row=0, sticky='W', padx=5)

my_machine = tk.Label(window, text="My Machine", font=dialogue_font)
my_machine.grid(column=0, row=1, sticky='W', padx=5)

official = tk.Label(window, text="Official Builds", font=dialogue_font)
official.grid(column=0, row=2, sticky='W', padx=5)

experimental = tk.Label(window, text="Experimental Builds", font=dialogue_font)
experimental.grid(column=0, row=3, sticky='W', padx=5)

def clicked():
    filePath = tk.filedialog.askopenfilename()
    print(filePath)
    return filePath

btn = tk.Button(window, text="Select File", command=clicked)
btn.grid(column=1, row=1)

window.mainloop()

