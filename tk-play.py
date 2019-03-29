import tkinter as tk
import tkinter.filedialog
import json
import subprocess
import TDInstallHelper

left_highlight          = "#808B96"
app_title               = "TouchDesigner Mulit-Version Manager"
window_size             = "1000x200"
header_font             = ("Arial Bold", 20)
dialogue_font           = ("Arial", 12)
btn_width               = 12
installer_btn_txt       = "Select File"
install_loc_txt         = "Select Location"
install_txt             = "Install"

window = tk.Tk()

# sets our window size
window.geometry(window_size)

# sets our window title
window.title(app_title)

install_header = tk.Label(window, text="Installs", font=header_font, pady=10)
install_header.grid(column=0, row=0, sticky='W', padx=5)

my_machine = tk.Label(window, text="My Machine", font=dialogue_font)
my_machine.grid(column=0, row=1, sticky='W', padx=5)

official = tk.Label(window, text="Official Builds", font=dialogue_font)
official.grid(column=0, row=2, sticky='W', padx=5)

experimental = tk.Label(window, text="Experimental Builds", font=dialogue_font)
experimental.grid(column=0, row=3, sticky='W', padx=5)

def return_file_path():
    filePath = tkinter.filedialog.askopenfilename()
    print(filePath)
    target_entry_str.set(filePath)
    return filePath

def return_dir_path():
    dirPath = tkinter.filedialog.askdirectory()
    print(dirPath)
    installer_loc_str.set(dirPath)
    return dirPath

def run_installer():
    source              = target_entry_str.get()
    target              = installer_loc_str.get()
    sub_p_cmd_str       = '{source} /extract {target}'.format(source=source, target=target)
    print(sub_p_cmd_str)
    pass

# target installer
target_installer_btn    = tk.Button(window, 
                                    text=installer_btn_txt, 
                                    command=return_file_path, 
                                    relief=tk.FLAT, 
                                    overrelief=tk.FLAT, 
                                    bg=left_highlight, 
                                    width=btn_width)
target_installer_btn.grid(column=1, row=1, sticky='W')

target_entry_str        = tk.StringVar()
target_entry            = tk.Entry(window, textvariable=target_entry_str, width=600)
target_entry.grid(column=3, row=1, padx=10)

# installer location
installer_loc_btn       = tk.Button(window, 
                                    text=install_loc_txt, 
                                    command=return_dir_path, 
                                    relief=tk.FLAT, 
                                    overrelief=tk.FLAT, 
                                    bg=left_highlight, 
                                    width=btn_width)
installer_loc_btn.grid(column=1, row=2, sticky='W')

installer_loc_str           = tk.StringVar()
installer_loc_entry     = tk.Entry(window, textvariable=installer_loc_str, width=600)
installer_loc_entry.grid(column=3, row=2, sticky='W', padx=10)

# install button - runs the subprocess cmd
install_btn             = tk.Button(window, 
                                    text=install_txt, 
                                    command=run_installer, 
                                    relief=tk.FLAT, 
                                    overrelief=tk.FLAT, 
                                    bg=left_highlight, 
                                    width=btn_width)
install_btn.grid(column=1, row=3, sticky='W')

# sets window icon
window.iconbitmap('assets/td.ico')

window.mainloop()