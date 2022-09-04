from task_functions import *


assert get_written_date(["04", "14", "2020"]) == 'April 14, 2020'
assert get_written_date(["06", "19", "2000"]) == 'June 19, 2000'
assert get_written_date(["12", "19", "2001"]) == 'December 19, 2001'
assert get_written_date(["01", "12", "1970"]) == 'January 12, 1970'
priority_scale = {1:"Lowest",2: "Low",3: "Medium",4:"High",5: "Highest"}

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
assert is_valid_day(["01", "02", "2022"]) == True
assert is_valid_day(["01", "52", "2022"]) == False
assert is_valid_year(["01", "02", "2022"]) == True
assert is_valid_year(["01", "02", "0022"]) == False

assert is_valid_priority("1", priority_scale) == True


assert is_valid_completion("yes") == True
assert is_valid_completion("nah") == False
assert is_valid_completion("no") == True


assert is_valid_name('bo') == False
assert is_valid_name('boo') == True

task = ["Finish Checkpoint 2 for CSW9", "Implement something old", "5", "06/05/2021", "nah"]
assert get_new_task(task,priority_scale) == ("name", "Finish Checkpoint 2 for CSW9")
dicty = ["Finish Chkpt 1 for CSW9", "Submit to Gauchospace", "5", "06/05/2021", "no"]


assert is_valid_index('0', ["Quizzes", 25.5]) == True
assert is_valid_index('1', ["Quizzes", 25.5]) == True
assert is_valid_index('2', ["Quizzes", 25.5]) == False
assert is_valid_index('0', ["Quizzes", 25.5]) == True
assert is_valid_index('1', ["Quizzes", 25.5]) == True
assert is_valid_index('2', ["Quizzes", 25.5]) == False

assert load_tasks_from_csv("test", [], priority_scale) == -1

assert load_tasks_from_csv("csv", [], priority_scale) == -1

assert save_tasks_to_csv([],'test') == -1
assert save_tasks_to_csv([],'.cs') == -1
assert save_tasks_to_csv([],'test.csv') == -1

assert delete_item([], [], start_idx=0) == 0
assert delete_item(['name'], [], start_idx="sad") == None
assert delete_item(['name'], {}, start_idx=0) == None

new_task_list = ['Book tickets', 'Verify dates', '3', '05/05/2022', 'no']
new_task_list_fail_completion = new_task_list[:]
new_task_list_fail_completion[4] = "Yes" # ensure case sensitive
assert get_new_task(new_task_list_fail_completion, priority_scale) == ("done", "Yes")

assert update_task([], 0, 0, 0,0, start_idx=0) == 0
assert update_task(all_tasks, -1, 0, 0, 0, start_idx=0) == -1
