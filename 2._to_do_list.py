tasks = [] # To-do list ke liye khaali list
while True: # while loop jo jab tak user quit na kare tab tak chalega
    action = input("kya karna hai? (add/view/quit): ").lower()
    # User se action poochhna
    if action == 'Add': # agar user 'add' karta hai
        task = input("Task likho: ")
        tasks.append(task)
        print(f'"{task}" task list me add ho gaya hai.')
    elif action == 'view': # agar user 'view' karta hai
        if not tasks: # agar list khali hai
            print("tak list khali hai.")
        else: # agar list me task hai 
            print("tumhare task list: ")
            for i, task in enumerate(tasks, 1): # enumerate se task ke sath uska number bhi milega
                print(f"{i}. {task}")
    elif action == 'quit': # agar user 'quit' karta hai
        print("To-do list se bahar nikal rahe hain. Alvida!")
        break # loop yaha ruck jayega 
    else: # agar user ne galat action diya
        print("Galat action! Kripya 'add', 'view', ya 'quit' me se koi ek chuno.")

# 📌 -------- Program Summary (Hinglish) --------
# 0. ✅ Is program me humne ye cheezein sikhin:
# 1. ✅ Ek khaali list banana aur usme items add karna (append)
# 2. ✅ while loop ka use karke program ko continuously chalana
# 3. ✅ if-elif-else ka use karke user ke input ke hisaab se action lena
# 4. ✅ enumerate() function se list ke items ko number ke sath dikhana
# 5. ✅ break statement ka use karke loop ko stop karna
# 6. ✅ User se input lena aur output ko clearly dikhana