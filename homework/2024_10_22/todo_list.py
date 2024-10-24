# TODO_LIST HOMEWORK

from os import system

tasks = []
system("clear")
while True:
    # menu
    action = int(input("\n   Menu\n" 
                       + "\t1 -> Add task\n"
                       + "\t2 -> Show tasks\n"
                       + "\t3 -> Remove task by tittle\n"
                       + "\t4 -> Remove task by number\n"
                       + "\t5 -> Clear TODO\n"
                       + "\t0 -> Exit\n"
                       ))
    print()
    match action:
        case 1:
            # add task
            task = input("New task tittle: ")
            if len(task) == 0:
                print("Error. Empty task tittle.")
            elif task not in tasks:
                tasks.append(task)  
            else:
                print("This task already exist!")
        case 2:
            # show tasks
            if len(tasks) == 0 :
                print(f"TODO list is empty.")
            else:
                print(f"TODO list ({len(tasks)}) :")
                for i in range(0, len(tasks)):
                    print(f"\t{i+1} --> {tasks[i]}") 
        case 3:
            # remove task by name
            if len(tasks) == 0 :
                print("TODO list is empty.")
            else:
                task_tittle = input("Enter task title for delete it : ")
                if task_tittle in tasks:
                    tasks.remove(task_tittle)
                else:
                    print(f"{task_tittle} not found in TODO list.")
        case 4:
            # remove task by number
            if len(tasks) == 0 :
                print("TODO list is empty.")
            else:
                task_number = int(input("Enter task number for delete it : "))
                if task_number <= 0 or task_number > len(tasks):
                    print(f"Not found task with number {task_number}.")
                else:
                    tasks.__delitem__(task_number - 1)

        case 5:
            # clear
            tasks.clear()
        case 0:
            break