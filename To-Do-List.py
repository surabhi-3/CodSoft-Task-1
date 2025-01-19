import tkinter as tk
from tkinter import messagebox

class TODOLIST:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def remove_task(self, task_num):
        task_num = int(task_num)
        if 1 <= task_num <= len(self.tasks):
            removed_task = self.tasks.pop(task_num - 1)
            return f"Task '{removed_task}' has been removed."
        else:
            return "Please Choose Task."

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List")
        self.root.geometry("400x400")

        self.todo_list = TODOLIST()

        # Label
        self.label = tk.Label(self.root, text="To-Do List", font=("Arial", 16))
        self.label.pack(pady=10)

        # Listbox to display tasks
        self.listbox = tk.Listbox(self.root, height=10, width=35, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Entry for adding tasks
        self.entry = tk.Entry(self.root, width=35)
        self.entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", width=20, command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Tasks", width=20, command=self.view_tasks)
        self.view_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Exit", width=20, command=self.quit)
        self.quit_button.pack(pady=10)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.todo_list.add_task(task)
            self.entry.delete(0, tk.END)  # Clear the entry
            self.update_listbox()
            messagebox.showinfo("Task Added", f"'{task}' has been added.")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def view_tasks(self):
        tasks = self.todo_list.view_tasks()
        if tasks:
            self.update_listbox()
        else:
            messagebox.showinfo("No Tasks", "Your to-do list is empty.")

    def remove_task(self):
        try:
            # Get the selected task index from the Listbox
            selected_task_index = self.listbox.curselection()[0]
            # Extract task number from the task string (e.g., "1. Task")
            task_to_remove = self.listbox.get(selected_task_index)  # Get the task text
            task_num = int(task_to_remove.split(".")[0])  # Extract task number from the string



            # Remove the task
            result = self.todo_list.remove_task(task_num)
            if "Task" in result:
                self.update_listbox()
                messagebox.showinfo("Task removed","{}".format(result))
            else:
                messagebox.showwarning("Your Choice Is Wrong -- Please Try Again--")

        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the Listbox
        tasks = self.todo_list.view_tasks()
        for idx, task in enumerate(tasks, 1):
            self.listbox.insert(tk.END, f"{idx}. {task}")  # Update the Listbox with tasks

    def quit(self):
        self.root.quit()

root = tk.Tk()
app = TodoApp(root)
root.mainloop()