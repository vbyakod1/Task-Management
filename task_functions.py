def print_main_menu(menu):
   """
print the menu options, a question on what you want to pick and some headers
   """
   print("==========================")
   print("What would you like to do?")
   for key,value in menu.items():
       print(f'{key} - {value}')
   print("==========================")



######## LIST OPTION ########
def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection





def print_task(task, priority_map, name_only = False):
   """prints the task under specific conditions and with specific formatting"""
   if name_only == True:
        print(task["name"])


   else:
      if task["info"] == "":
         print(task["name"])
         formatteddate = get_written_date(task["duedate"].split("/"))
         print(f'  * Due: {formatteddate}  (Priority: {priority_map[int(task["priority"])]})')
         print(f'  * Completed? {task["done"]}')

      else:
         print(task["name"])
         print(f'  * {task["info"]}')
         formatteddate = get_written_date(task["duedate"].split("/"))
         print(f'  * Due: {formatteddate}  (Priority: {priority_map[int(task["priority"])]})')
         print(f'  * Completed? {task["done"]}')

   return 
            
        

def get_written_date(date_list):
   """converts date into a written format with slashes"""
   month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
   if len(date_list) == 3:
      month = date_list[0]
      month = month_names[int(month)]
      day = date_list[1]
      day = int(day)
      year = date_list[2]
      result = f'{month} {day}, {year}'
      return result
   else:
      month = date_list[0]
      month = month_names[int(month)]
      year = date_list[1]
      result = f'{month},{year}'
      return result
   
  

def print_tasks(task_list, priority_map, name_only = False,
                show_idx = False, start_idx = 0, completed = "all"):
    """
    param: task_list (list) - a list containing dictionaries with
            the task data
    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed 
            for the priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.
            Passed as an argument into the helper function.
    param: show_idx (Boolean) - by default, set to False.
            If False, then the index of the task is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            task name.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets displayed for the first task, if show_idx is True.
    param: completed (str) - by default, set to "all".
            By default, prints all tasks, regardless of their
            completion status ("done" field status).
            Otherwise, it is set to one of the possible task's "done"
            field's values in order to display only the tasks with
            that completion status.

    returns: None; only prints the task values from the task_list

    Helper functions:
    - print_task() to print individual tasks
    """
    print("-"*42)
    for tasks in task_list: # go through all tasks in the list
        if show_idx == True:
              print(f"{start_idx}.", end=" ")
              start_idx = start_idx+1
        if completed == "all":
            print_task(tasks, priority_map, name_only)
        elif tasks["done"] == completed:
            print_task(tasks, priority_map, name_only)
        
def is_valid_index(idx, in_list, start_idx = 0):
   """checks if the index is valid and then returns True/False as a result"""
   if str(idx).isdigit():
      idx = int(idx)
      idx -= start_idx
      if idx >= 0 and idx < len(in_list):
         return True
   return False

def delete_item(in_list, idx, start_idx = 0):
   """deletes category of the tasks from the menu"""
   if not in_list:
      return 0

   elif (type(start_idx) != int) or (type(idx) != str):
      return None
   
   elif is_valid_index(idx, in_list, start_idx) == False:
      return -1
   else:
      idx = int(idx)-start_idx
      return in_list.pop(int(idx))

def update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0):
   """updates task to append with validation checks included as well"""
   new_idx=int(idx)-start_idx
   if info_list == []:
      return 0
   elif is_valid_index(idx, info_list) == False:
      return -1
   
   if field_key == "name":
      if is_valid_name(field_info) == True:
         task = info_list[new_idx]
         task[field_key] = field_info
         info_list[new_idx] = task
         return info_list[new_idx]
      else:
         if is_valid_name(field_info) == False:
            return field_key
         
   elif field_key == "info":
         task = info_list[new_idx]
         task[field_key] = field_info
         info_list[new_idx] = task
         return info_list[new_idx]
      
      
   elif field_key == "priority":
      if is_valid_priority(field_info, priority_map) == True:
         task = info_list[new_idx]
         task[field_key] = field_info
         info_list[new_idx] = task
         return info_list[new_idx]
      else:
         return field_key

      
   elif field_key == "duedate":
      if is_valid_date(field_info) == True:
         task = info_list[new_idx]
         task[field_key] = field_info
         info_list[new_idx] = task
         return info_list[new_idx]
      else:
         if is_valid_date(field_info) == False:
            return field_key

      
   elif field_key == "done":
      if is_valid_completion(field_info) == True:
         task = info_list[new_idx]
         task[field_key] = field_info
         info_list[new_idx] = task
         return info_list[new_idx]
      else:
         if is_valid_completion(field_info) == False:
            return field_key
   else:
      return -2
   





  
            
            
def is_valid_name(task):
   """validates the name and then returns T or F"""



   
   if type(task) == str:
      if 3 <= len(task) <= 25:
         return True
      else:
         return False
   else:
      return False

def is_valid_completion(task):
   """validates yes or no for task"""


   
   if type(task) == str:
      if "yes" in task or "no" in task:
         return True
      else:
         return False
   else:
      return False
    
   
def is_valid_month(date_list):
   """checks if it is a valid month and then returns T or F"""
   if type(date_list[0]) == str:
      if 1 <= int(date_list[0]) <= 12:
         return True
      else:
         return False
    
def is_valid_day(date_list):
   """checks if it is a valid day and then returns T or F"""
   num_days = { 
        
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
   days = 0
   if is_valid_month(date_list) == True:
      days = num_days[int(date_list[0])]
      if 0 < int(date_list[1]) <= days:
         return True
      else:
         return False
   
   
    

    
    
   

def is_valid_year(date_list):
   """checks if it is a valid year and then returns T or F"""
   if type(date_list[-1]) == str:
      if int(date_list[-1]) > 1000:
         return True
      else:
         return False

def is_valid_priority(string, dictionary):
   """validates the priority using the dictionary given"""
   if type(string) != str or type(dictionary) != dict:
      return False
   else:
      if string.isdigit() == True:
         if int(string) in dictionary.keys():
            return True
      else:
         return False

def is_valid_date(date_string):
   """gets date validation through checking the other components and validating them"""
   if len(date_string) > 1:
      initialize = date_string.split("/")
      month = is_valid_month(initialize)
      date = is_valid_day(initialize)
      year = is_valid_year(initialize)
      if month == True and date == True and year == True:
         return True
      else:
         return False
   else:
      return False




def get_new_task(cats, dictionary):
   """gets new task using append and the validation checks of the name, etc"""
   dic = {
      "name":"",
      "info":"",
      "priority":"",
      "duedate":"",
      "done":""
      }
   length = len(cats)
   if length > 3 and length < 6:
      if is_valid_name(cats[0]) == True:
         dic["name"] = cats[0]
      else:
         return ("name", cats[0])
      if length == 5:
         dic["info"] = cats[1]
         if is_valid_date(cats[3]) == True:
            dic["duedate"] = cats[3]
         else:
            return ('duedate', cats[3])
         if is_valid_priority(cats[2], dictionary) == True:
            dic["priority"] = int(cats[2])
         else:
            return ('priority', (cats[2]))
         if is_valid_completion(cats[4]) == True:
            dic["done"] = cats[4]
         else:
            return ('done', cats[4])
      elif length == 4:

         if is_valid_priority(cats[1], dictionary) == True:
            dic["priority"] = int(cats[1])
         else:
            return ('priority', (cats[1]))
         if is_valid_date(cats[2]) == True:
            dic["duedate"] = cats[2]
         else:
            return ("duedate", cats[2])
         if is_valid_completion(cats[3]) == True:
            dic["done"] = cats[3]

         else:
            return ('done', cats[3])
      return dic
   else:
      return length
         
            

   

def load_tasks_from_csv(filename, in_list, priority_map):
   """aids the restore function int the main by loading tasks from csv"""
   import csv
   import os
   if filename[-4:] != '.csv':
      return -1
   elif os.path.exists(filename) == False:
      return None
   else:
      newlist = []
      with open(filename, 'r') as file:
         csvreader = csv.reader(file)
         pos = 1
         for row in csvreader:
            result = get_new_task(row, priority_map)
            if type(result) == dict:
               in_list.append(result)
            else:
               newlist.append(pos)
            pos += 1
      return newlist
   
   
def save_tasks_to_csv(tasks_list, filename):
   """saves tasks to a csv file and appends it to a list"""
   import csv
   if filename[-1:-5] == '.csv':
      with open(filename,'w', newline='') as csvfile:
         csv_writer = csv.writer(csvfile)
         new = []
         for task in tasks_list:
            new.append(task)
            csv.writerow(new)
   else:
      return -1
   

   


   
