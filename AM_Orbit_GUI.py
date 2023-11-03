# -*- encoding: utf-8 -*-

# Author: ChengWei Sun
# Created on 2021/11/03
# Description: GUI AM_Orbit 
# Todos:
# 1. import the LMIO and MPP module
# 2. modify the run_function() to run the MPP.main() function

## install the theme package
# conda create -c conda-forge -n tkgui python 
# pip install ttkthemes
## activate the environment
# conda activate tkgui

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk

# Create the main window
root = ThemedTk(theme="black")

# Set the window title
root.title("AM_orbit_GUI by CWSun")

# Set the window size
root.geometry("1000x300")  # Width x Height

# Create a StringVar for each file path
dem_file = tk.StringVar()
csv_file = tk.StringVar()
output_folder = tk.StringVar()
return_value = tk.StringVar()

# Create a function to open the file dialog for dem file
def open_dem_file():
    file = filedialog.askopenfilename()
    dem_file.set(file)

# Create a function to open the file dialog for csv file
def open_csv_file():
    file = filedialog.askopenfilename()
    csv_file.set(file)

# Create a function to open the directory dialog for output folder
def open_output_folder():
    folder = filedialog.askdirectory()
    output_folder.set(folder)

# Create a function to run the file
def run_function():
    dem = dem_file.get()
    csv = csv_file.get()
    output = output_folder.get()
    if dem and csv and output:
        result = f"Running function with: {dem}, {csv}, {output}"
        print(result)
        return_field.delete(1.0, tk.END)
        return_field.insert(tk.END, result)
    else:
        error = "Please select all files and output folder"
        print(error)
        # overwrite the text field
        return_field.delete(1.0, tk.END)
        return_field.insert(tk.END, error)

# Define the witdth of the text field
displayCharacters = 100
# Define the button width
button_width = 20


# Create the label for 'description'
description_label = ttk.Label(root, text="Description", width=button_width)
description_label.grid(row=0, column=0)

# Create the text field for descriptions
description_field = tk.Text(root, width=displayCharacters, height=2)
description_field.grid(row=0, column=1)
# set the text for the description field
description_field.insert(1.0, "Choose a DEM file, a CSV file, and an output folder using left buttoms, then click Run.")
description_field.config(state="disabled")

# Add a separator
separator1 = ttk.Separator(root, orient="horizontal")
separator1.grid(row=1, column=0, columnspan=2, sticky='ew')

# Create the file selection button for dem file
select_dem_button = ttk.Button(root, text="Select DEM File", command=open_dem_file, width=button_width)
select_dem_button.grid(row=2, column=0)

# Create the text field for dem file path
dem_field = ttk.Entry(root, textvariable=dem_file, width=displayCharacters)
dem_field.grid(row=2, column=1)

# Create the file selection button for csv file
select_csv_button = ttk.Button(root, text="Select CSV File", command=open_csv_file, width=button_width)
select_csv_button.grid(row=3, column=0)

# Create the text field for csv file path
csv_field = ttk.Entry(root, textvariable=csv_file, width=displayCharacters)
csv_field.grid(row=3, column=1)

# Create the folder selection button for output folder
select_output_button = ttk.Button(root, text="Select Output Folder", command=open_output_folder, width=button_width)
select_output_button.grid(row=4, column=0)

# Create the text field for output folder path
output_field = ttk.Entry(root, textvariable=output_folder, width=displayCharacters)
output_field.grid(row=4, column=1)

# Create the run button
run_button = ttk.Button(root, text="Run", command=run_function, width=button_width)
run_button.grid(row=5, column=1)

# Add a separator
separator2 = ttk.Separator(root, orient="horizontal")
separator2.grid(row=6, column=0, columnspan=2, sticky='ew')

# Create the text field for return value
return_label = ttk.Label(root, text="Return Value", width=button_width)
return_label.grid(row=7, column=0)

# Create the Text widget for the return value at the bottom
return_field = tk.Text(root, width=displayCharacters, height=5)
return_field.grid(row=7, column=1)

# Start the main loop
root.mainloop()