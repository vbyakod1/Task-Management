from task_functions import *


the_menu = {
    "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"
}   

all_tasks = [
    {
        "name": "Call XYZ",
        "info": "",
        "priority":3,
        "duedate": '05/28/2022',
        "done": 'yes'
    },
    {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority":5,
        "duedate": '06/02/2022',
        "done": 'no'
    },
    {
        "name": "Finish checkpoint 2 for CSW8",
        "info": "Implement the new functions",
        "priority":5,
        "duedate": '06/05/2022',
        "done": 'no'
    }

]

list_menu = {
    "A": "all tasks",
    "C": "completed tasks",
    "I": "incomplete tasks"
}

priority_scale = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}
opt = None

while True:
    print_main_menu(the_menu) 
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() 

    if opt not in the_menu.keys(): 
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'q' or opt == 'Q': 
        print("Goodbye!\n")
        break
    
    elif opt == 'L':
        if all_tasks == []:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input = ("::: Press Enter to continue")
            continue
        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_tasks(all_tasks, priority_scale)
        elif subopt == 'C':
            print_tasks(all_tasks, priority_scale, completed = 'yes')
        elif subopt == 'I':
            print_tasks(all_tasks, priority_scale, completed = 'no')

    elif opt == 'D':
        continue_action='y'
        while continue_action=='y':
            if all_tasks == []:
                print("WARNING:There is nothing to delete!")
                break
            print("Which task would you like to delete?")
            print("A - Delete all tasks at once")
            print_tasks(all_tasks, priority_scale, name_only = True, show_idx = True, start_idx = 1)
            print("::: Enter the number corresponding to the task.")
            print(" or press 'M' to return to the main menu.")
            user_option = input("> ")
            if is_valid_index(user_option, all_tasks, 1) == True:
                idx = int(user_option)-1
                result = all_tasks[idx]["name"]
                delete_item(all_tasks, user_option, 1)
                print(f"Success!\nDeleted the task |{result}|")
                all_tasks.pop(idx)
            elif user_option == "A":
                print("::: WARNING! Are you sure you want to delete all tasks?")
                print("::: Type Yes to continue the deletion.")
                userop2=input("> ")
                if userop2 == "Yes"or "YES" or "yes":
                    all_tasks.clear()
                    print("Deleted all tasks.")
                    break
            elif user_option == "M":
                break
            else:
                print(f"WARNING: |{user_option}| is an invalid task number!")

            print("::: Would you like to delete another task?", end = " ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()    

    elif opt == "U":
        continue_action = 'y'
        while continue_action == 'y':
            if all_tasks == []:
                print("WARNING: There is nothing to update!")
                break
            print("::: Which task would you like to update?")
            print_tasks(all_tasks, priority_scale, name_only = True, show_idx = True, start_idx = 1)
            print("::: Enter the number corresponding to the task.")
            user_option = input("> ")
            if is_valid_index(user_option, all_tasks, 1) == True:
                idx = int(user_option)-1
                subopt = get_selection("update", all_tasks[idx], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") 
                field_info = input("> ")
                result = update_task(all_tasks, user_option, priority_scale, subopt, field_info, start_idx = 1)
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")  
                    print_task(result, priority_scale)  
                else: # update_task() returned an error
                    print(f"WARNING: invalid information for the field |{field_info}|!") 
                    print(f"The task was not updated.")
            else: # is_valid_index() returned False
                print(f"WARNING: |{user_option}| is an invalid task number!")

            print("::: Would you like to update another task?", end = " ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      
            # -------------------------------------------------

    elif opt == "A":
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter each required field, separated by commas.")
            print("::: name, info, priority, MM/DD/YYYY, is task done? (yes/no)")
            task_info = input("> ")
            new_task = task_info.split(',')
            result = get_new_task(new_task, priority_scale)
            if type(result) == dict:
                all_tasks.append(result)
                print(f"Successfully added a new task!")
                print_task(result, priority_scale)
            elif type(result) == int:
                print(f"WARNING: invalid number of fields!")
                print(f"You provided {result}, instead of the expected 5.\n")
            else:
                print(f"WARNING: invalid task field: {result}\n")

            print("::: Would you like to add another task?", end = " ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower() 
            # ----------------------------------------------------------------
                
    
    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            new = save_tasks_to_csv(all_tasks, filename)
            if new == -1: 
                print(f"WARNING: |{filename}| is an invalid file name!") 
                print("::: Would you like to try again?", end = " ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the tasks to |{filename}|")



            
    #--------------------------------------------------------------------------
                
                
    elif opt == "R":
        continue_action = 'y'
        while continue_action == "y":
            print("::: Enter the filename ending with '.csv'.")
            filenames = input("> ")
            result = load_tasks_from_csv(filenames, all_tasks, priority_scale)
            if type(result) == list or []:
                print(f"Successfully stored all the tasks to |{filenames}|")
            else:
                print(f"WARNING: |{filenames}| was not found!") 
                print("::: Would you like to try again? Enter 'y' to try again.", end = " ")
                continue_action = input("\n> ")
                continue_action = continue_action.lower()
                    
            
            
                
                
                
                               
                
                
        

         
    input("::: Press Enter to continue")

print("Have a nice day!")
