#to do list
import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to update/edit task
def update_task():
    try:
        index = listbox.curselection()
        updated_task = entry.get()
        if updated_task:
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Function to mark the selected task as finish
def mark_as_finish():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        updated_task = task + " (finish)"
        listbox.delete(index)
        listbox.insert(index, updated_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# main function
root = tk.Tk()
root.title("To-Do List")


# Create the to-do list
listbox = tk.Listbox(root, width=40, height=20, font=("Arial", 12))
listbox.pack(pady=20)

# Create the scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add the scrollbar to the to-do list
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create the task entry field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=20)

# Create buttons to add, delete, update, and mark as done tasks
add_button = tk.Button(root, text="ADD TASK", command=add_task)
add_button.pack(pady=5)
delete_button = tk.Button(root, text="DELETE TASK", command=delete_task)
delete_button.pack(pady=5)
update_button = tk.Button(root, text="UPDATE TASK", command=update_task)
update_button.pack(pady=5)
mark_done_button = tk.Button(root, text="MARK AS FINISH", command=mark_as_finish)
mark_done_button.pack(pady=5)

# Start the GUI main loop
root.mainloop()
