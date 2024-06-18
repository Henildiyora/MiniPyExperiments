class ToDoList:
    def __init__(self):
        """
        Initializes the ToDoList class with an empty task list.
        """
        self.tasks = []

    def add_task(self, task: str) -> None:
        """
        Adds a task to the to-do list.

        Args:
            task (str): The task description.
        """
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")

    def complete_task(self, task_index: int) -> None:
        """
        Marks a task as completed.

        Args:
            task_index (int): The index of the task to mark as completed.
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task '{self.tasks[task_index]['task']}' marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index: int) -> None:
        """
        Deletes a task from the to-do list.

        Args:
            task_index (int): The index of the task to delete.
        """
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' deleted from the list.")
        else:
            print("Invalid task index.")

    def view_tasks(self) -> None:
        """
        Displays all tasks in the to-do list.
        """
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i + 1}. {task['task']} - {status}")


if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Complete task")
        print("3. Delete task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task = input("Enter task description: ").strip()
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.complete_task(index)
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid option. Please choose a valid option.")
