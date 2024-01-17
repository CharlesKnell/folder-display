# tag=charlesknell -- Folder Display 2.2

import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from recursive_listing import list_files
from tkinter import ttk


def clear():
    text_widget.delete(1.0, END)


def select_a_directory_and_print():
    count = 0
    if not checkbox_include_subfolders.get():
        dir_path = filedialog.askdirectory()
        dir_list = os.listdir(dir_path)
        if not checkbox_show_full_path.get():
            dir_path = dir_path.replace("/", "\\")
            text_widget.insert(tk.END, dir_path + "\n\n")
        for filename in dir_list:
            count += 0.05
            progress_bar['value'] = count
            progress_bar.update()
            if not checkbox_show_full_path.get():
                text_widget.insert(tk.END, filename + "\n")
            else: # checkbox_show_full_path is checked
                full_path = dir_path + "\\" + filename + "\n"
                full_path = full_path.replace("/", "\\")
                text_widget.insert(tk.END, full_path)

    else:  # the checkbox include subfolders is checked
        dir_path = filedialog.askdirectory()
        dir_path = dir_path.replace("/", "\\")
        if not checkbox_show_full_path.get():
            text_widget.insert(tk.END, dir_path + "\n\n")
        list1 = list_files(dir_path, count, progress_bar)

        for filename in list1:
            count += 0.05
            if not checkbox_show_full_path.get():
                filename = filename.replace(dir_path + "\\", "")
                text_widget.insert(tk.END, filename + "\n")
            else:  # checkbox show full path is checked
                # filename = filename.replace("/", "\\")
                text_widget.insert(tk.END, filename + "\n")
            progress_bar['value'] = count
            progress_bar.update()
    progress_bar['value'] = 0
    progress_bar.update()


def open_author_link(event):
    import webbrowser
    webbrowser.open(author_link)


def open_donate_link(event):
    import webbrowser
    webbrowser.open(donate_link)


window = tk.Tk()

button1 = tk.Button(text="Select Folder", command=select_a_directory_and_print)
button1.config(bd=3)
button1.grid(row=0, column=0, padx=20, pady=10)

checkbox_include_subfolders = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Include Subfolders", variable=checkbox_include_subfolders)
checkbox.grid(row=0, column=1, padx=0, pady=10)
checkbox.config(bg="lightgrey")

checkbox_show_full_path = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Show Full Path", variable=checkbox_show_full_path)
checkbox.grid(row=0, column=2, padx=0, pady=10)
checkbox.config(bg="lightgrey")

button2 = tk.Button(text="Clear Display", command=clear)
button2.config(bd=3)
button2.grid(row=0, column=3, padx=0, pady=10)

author_label = tk.Label(window, text="Author: Charles Knell", cursor="hand2")
author_label.config(bd=3)
author_label.grid(row=0, column=4, padx=20, pady=10)

donate_label = tk.Label(window, text="Donate - Thank You", cursor="hand2")
donate_label.config(bd=3)
donate_label.grid(row=3, column=0, padx=20, pady=10)

text_widget = tk.Text(window, width=107, height=40, wrap='none')

scrollbar_v = tk.Scrollbar(window, command=text_widget.yview, orient=tk.VERTICAL)
scrollbar_v.grid(row=1, column=5, sticky='NS', padx=0)
scrollbar_h = tk.Scrollbar(window, command=text_widget.xview, orient=tk.HORIZONTAL)
scrollbar_h.grid(row=2, column=0, padx=(30, 0), pady=(0, 10), sticky=tk.EW, columnspan=5)

text_widget.config(yscrollcommand=scrollbar_v.set)
text_widget.config(xscrollcommand=scrollbar_h.set)
text_widget.grid(row=1, column=0, padx=(30, 0), pady=0, columnspan=5, sticky='nsew')

author_link = "https://www.linkedin.com/in/charlesknell/"
author_label.bind("<Button-1>", open_author_link)

donate_link = "http://charlesknell.net/send-me-a-tip-thank-you/"
donate_label.bind("<Button-1>", open_donate_link)

window.title("Folder Display 2.2")
window.geometry("940x770")  # set window size
window.config(bg="lightgrey")
window.columnconfigure(5, minsize=0)

progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="indeterminate")
progress_bar.grid(row=3, column=0, pady=10, columnspan=6)

window.mainloop()
