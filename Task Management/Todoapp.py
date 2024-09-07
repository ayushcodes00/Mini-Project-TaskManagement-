def task():#creating function

    tasks = [] #empty set
    print("----Welcome to Task Management App----")

    total_task = int(input("Enter how many task you want to Add "))#asking user to input the task

    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's task are\n{tasks}")#all the task of the user is printed

    while True:
        operation = int(input("Enter 1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop "))

        if operation == 1 :#if user wants to add
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been sucessfully added.")

        elif operation == 2:#if user wants to update
            updated_tsk = input("Enter the task you want to update = ")
            if updated_tsk in tasks:
                up = input("Enter new Task = ")
                ind = tasks.index(updated_tsk)
                tasks[ind] = up
                print(f"Updated task {up}")
        
        elif operation == 3:#if user wants to delete
            del_t = input("Which task you want to delete = ")
            if del_t in tasks:
                ind = tasks.index(del_t)
                del tasks[ind]
                print(f"Task {del_t} has been deleted")
        
        elif operation == 4:#if user wants to view all tasks
            print(f"All tasks = {tasks}")

        elif operation == 5:#if user wants to close the program
            print("Closing the Program")
            break
        
        else:#if user enters other than 1,2,3,4,5
            print("Invalid Input")

task()

                
