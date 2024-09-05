def task():
    tasks = []
    print("====Welcome to todo list====")
    
    total_task = int(input("Enter how many task you want to print "))
    for i  in range(1,total_task+1):
          task_name = input(f"Enter task {i}")
          tasks.append(task_name)
    print(f"Today tasks are\n  {tasks}") 
    while True:
         operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-Show\n5-Exit/Stop/"))
         if operation==1:
          add = input("Enter  a task you want to add")
          tasks.append(add)
          print(f"Task {add} has been Succesfully added...")
         elif  operation==2:
          update_val = input("Enter a task you want to update")
          if update_val in tasks:
                up = input("Enter new task here")
                ind = tasks.index(update_val)
                tasks[ind] =  up
                print(f"Your updated task {up}")
         elif operation==3:
               delete = input("Enter a task you want to  delete")
               if delete in tasks:
                     ind = tasks.remove(delete)
                     print(f"Task {delete} has been deleted ")
               else:
                     print("Task not found")
         elif operation==4:
               print(f"Today tasks are {tasks}")
         elif operation==5:
               print("Closing the program")
               break
               
task()               