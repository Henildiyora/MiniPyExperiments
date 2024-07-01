import sqlite3

class ToDoList:
    def __init__(self, db_name="todo_list.db"):
        """
        Initializes the ToDoList class and sets up the database connection.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
            )
        ''')
        self.conn.commit()

    def add_task(self, task: str) -> None:
        """
        Adds a task to the to-do list.

        Args:
            task (str): The task description.
        """
        self.cursor.execute('''
            INSERT INTO tasks (task, completed) VALUES (?, ?)
        ''', (task, False))
        self.conn.commit()
        print(f"Task '{task}' added to the list.")

    def complete_task(self, task_id: int) -> None:
        """
        Marks a task as completed.

        Args:
            task_id (int): The ID of the task to mark as completed.
        """
        self.cursor.execute('''
            UPDATE tasks SET completed = ? WHERE id = ?
        ''', (True, task_id))
        self.conn.commit()
        print(f"Task ID '{task_id}' marked as completed.")

    def delete_task(self, task_id: int) -> None:
        """
        Deletes a task from the to-do list.

        Args:
            task_id (int): The ID of the task to delete.
        """
        self.cursor.execute('''
            DELETE FROM tasks WHERE id = ?
        ''', (task_id,))
        self.conn.commit()
        print(f"Task ID '{task_id}' deleted from the list.")

    def view_tasks(self) -> None:
        """
        Displays all tasks in the to-do list.
        """
        self.cursor.execute('SELECT id, task, completed FROM tasks')
        tasks = self.cursor.fetchall()
        if not tasks:
            print("No tasks in the list.")
        else:
            for task in tasks:
                status = "Completed" if task[2] else "Not Completed"
                print(f"ID: {task[0]}, Task: {task[1]}, Status: {status}")

    def __del__(self):
        """
        Closes the database connection when the ToDoList object is deleted.
        """
        self.conn.close()

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

        if choice == '1':
            task = input("Enter task description: ").strip()
            todo_list.add_task(task)
        elif choice == '2':
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.complete_task(task_id)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid option. Please choose a valid option.")
