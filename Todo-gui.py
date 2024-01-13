#! python3
import tkinter as tk
from tkinter import messagebox, simpledialog  # Import simpledialog
import json

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        # Load tasks from JSON file
        self.tasks = self.load_tasks()

        # Create GUI elements
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=10)

        self.refresh_task_listbox()

        add_button = tk.Button(master, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        delete_button.pack(side=tk.RIGHT, padx=5)

        quit_button = tk.Button(master, text="Quit", command=self.master.destroy)
        quit_button.pack(side=tk.RIGHT, padx=5)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = {"tasks": []}
        return tasks

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

    def refresh_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks["tasks"]:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        new_task = simpledialog.askstring("Add Task", "Enter the task:")
        if new_task:
            self.tasks["tasks"].append(new_task)
            self.save_tasks()
            self.refresh_task_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            deleted_task = self.tasks["tasks"].pop(task_index)
            self.save_tasks()
            self.refresh_task_listbox()
            messagebox.showinfo("Task Deleted", f"Task '{deleted_task}' deleted successfully.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
