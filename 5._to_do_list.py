
e
# Step 1: Program shuru hote hi file se tasks load karo
tasks = load_tasks_from_file()

# Step 2: Manager (while loop) ko shuru karo
while True:
    action = input("kya karna hai? (add/view/remove/edit/quit): ").lower()

    if action == 'add':
        add_task(tasks)  # 'add' kaam ke liye add_task worker ko bulao

    elif action == 'view':
        view_tasks(tasks)  # 'view' kaam ke liye view_tasks worker ko bulao

    elif action == 'remove':
        remove_task(tasks)

    elif action == 'edit':
        edit_task(tasks)

    elif action == 'quit':
        save_tasks_to_file(tasks)  # Program band karne se pehle save worker ko bulao
        print("Task list ko 'task.txt' me save kar diya gaya hai.")
        break

    else:
        print("Galat action! Kripya sahi command chuno.")
