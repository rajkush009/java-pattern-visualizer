tasks = [] # To-do list ke liye khaali list
while True: # while loop jo jab tak user quit na kare tab tak chalega
    action = input("kya karna hai? (add/view/remove/edit/quit): ").lower()
    # User se action poochhna
    if action == 'add': # agar user 'add' karta hai
        task = input("Task likho: ")
        tasks.append(task) # task ko list me add karna 
        print(f'"{task}" task list me add ho gaya hai.') # confirmation message
    elif action == 'view': # agar user 'view' karta hai
        if not tasks: # agar list khali hai
            print("tak list khali hai.") 
        else: # agar list me task hai 
            print("tumhare task list: ")
            for i, task in enumerate(tasks, 1): # enumerate se task ke sath uska number bhi milega
                print(f"{i}. {task}")
    elif action == 'remove': # agar user 'remove' karta hai
        if not tasks: # agar list khanli hai
            print("Task list khali hai, kuch remove nahi kar sakte ")
        else: # agar list me task hai
            task_number = int(input("Kaunsa task number remove karna hai? : ")) # user se task number poochhna
            if 1 <= task_number <= len(tasks): # sahi number hai ya nahi
                removed_task = tasks.pop(task_number - 1)
                print(f'"{removed_task}" task list se remove kar diya gaya hai.')
            else: # galat number diya hai
                print("Galat task number! Kripya sahi number daalo.") 
    elif action == 'edit': # agar user 'edit' karta hai
        if not tasks: # agar list khanli hai
            print("Task list khali hai, kuch edit nahi kar sakte ")
        else: # agar list me task hai
            task_number = int(input("Kaunsa task number edit karna hai? : "))
            if 1 <= task_number <= len(tasks): # sahi number hai ya nahi
                new_task = input("Naya task likho: ")
                tasks[task_number - 1] = new_task
                print(f'Task number {task_number} ko update kar diya gaya hai.')
            else: # galat number diya hai
                print("Galat task number! Kripya sahi number daalo.")
    elif action == 'quit': # agar user 'quit' karta hai
        print("To-do list se bahar nikal rahe hain. Alvida!")
        break # loop yaha ruck jayega 
    else: # agar user ne galat action diya
        print("Galat action! Kripya 'add', 'view', 'remove', 'edit' ya 'quit' me se koi ek chuno.") 
# Overall, is program me:
#List manipulation (add/remove/update)
#Looping
#Conditional logic
#User input handling
#Error checking
#Clear output display
