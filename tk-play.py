from tkinter import *
import tkinter.filedialog
import json
import subprocess

left_highlight      = "#808B96"
app_title           = "TouchDesigner Mulit-Version Manager"
window_size         = "1000x200"
header_font         = ("Arial Bold", 20)
dialogue_font       = ("Arial", 12)
btn_width           = 12
installer_btn_txt   = "Select File"
install_loc_txt     = "Select Location"
install_txt         = "Install"

window = Tk()

# sets our window size
window.geometry(window_size)

# sets our window title
window.title(app_title)

install_header = Label(window, text="Installs", font=header_font)
install_header.grid(column=0, row=0, sticky='W', padx=5)

my_machine = Label(window, text="My Machine", font=dialogue_font)
my_machine.grid(column=0, row=1, sticky='W', padx=5)

official = Label(window, text="Official Builds", font=dialogue_font)
official.grid(column=0, row=2, sticky='W', padx=5)

experimental = Label(window, text="Experimental Builds", font=dialogue_font)
experimental.grid(column=0, row=3, sticky='W', padx=5)

def return_file_path():
    filePath = tkinter.filedialog.askopenfilename()
    print(filePath)
    return filePath

def return_dir_path():
    dirPath = tkinter.filedialog.askdirectory()
    print(dirPath)
    return dirPath

def run_installer():
    pass

# target installer
target_installer_btn    = Button(window, text=installer_btn_txt, command=return_file_path, relief=FLAT, overrelief=FLAT, bg=left_highlight, width=btn_width)
target_installer_btn.grid(column=1, row=1, sticky='W')

target_entry            = Entry(window,width=600)
target_entry.grid(column=3, row=1)

# installer location
installer_loc_btn       = Button(window, text=install_loc_txt, command=return_dir_path, relief=FLAT, overrelief=FLAT, bg=left_highlight, width=btn_width)
installer_loc_btn.grid(column=1, row=2, sticky='W')

installer_loc_entry     = Entry(window,width=600)
installer_loc_entry.grid(column=3, row=2, sticky='W')

# install button - runs the subprocess cmd
install_btn             = Button(window, text=install_txt, command=run_installer, relief=FLAT, overrelief=FLAT, bg=left_highlight, width=btn_width)
install_btn.grid(column=1, row=3, sticky='W')

# sets window icon
window.iconbitmap('assets/td.ico')

window.mainloop()

