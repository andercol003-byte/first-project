tasks = []  

while True:
    print("\nMenu:")
    print("1. Add task")
    print("2. Enter completed tasks")
    print("3. Print final list")
    print("4. Quit")

    choice = input("Choose an option: ")
    
    if choice == "1":
        while True:
            task_name = input("Put task name here, or q to quit")
            if task_name.lower() == "q":
                break

            priority = input ("Priority(high, low, medium): ")

            task = {
            "Name" : task_name, 
            "Priority" : priority,
            "Done?" : False
            }
            tasks.append(task)

    elif choice == "2":
        for i in range(len(tasks)):
            current_task = tasks[i]
            print(i + 1 , ":")
            print(current_task["Name"])
            print("Priority:", current_task["Priority"])
            print("Done?", current_task["Done?"])
            print(
            )
        while True:
            tasknum = input("Which task is complete? (0 to return to menu)")
            if type(tasknum) != "Integer":
                print("put in a number")
            elif tasknum == "0":
                break
            elif int(tasknum) <= len(tasks) and int(tasknum)>= 1:
                task_index = int(tasknum) - 1
                selected_task = tasks[task_index]
                selected_task["Done?"] = True
            else:
                print("Try again, no task found")

    elif choice == "3":
        for i in range(len(tasks)):
            current_task = tasks[i]
            print(i + 1 , ":")
            print(current_task["Name"])
            print("Priority:", current_task["Priority"])
            print("Done?", current_task["Done?"])
            print(
            )

    elif choice == "4":
        break

    else:
        print("Invalid option, try again.")

