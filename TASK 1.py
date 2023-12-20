import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.load_tasks_from_file()  # Load tasks from a file if available

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="To-Do List")
        self.label.pack()

        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(self.root, width=40)
        self.listbox.pack()

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks_to_file)
        self.save_button.pack()

        self.load_tasks_from_file()  # Display loaded tasks

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"description": task, "completed": False})
            self.list_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.list_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[index]["description"] = updated_task
                self.list_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def list_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            task_status = " [X]" if task["completed"] else " [ ]"
            self.listbox.insert(tk.END, f"{task['description']}{task_status}")

    def save_tasks_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['description']},{task['completed']}\n")
        messagebox.showinfo("Saved", "Tasks saved to file.")

    def load_tasks_from_file(self):
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    task_data = line.strip().split(',')
                    task_description = task_data[0]
                    task_completed = True if task_data[1] == "True" else False
                    self.tasks.append({"description": task_description, "completed": task_completed})
                self.list_tasks()
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "No saved tasks found.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
