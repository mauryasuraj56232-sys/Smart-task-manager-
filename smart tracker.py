import json
import os

class Task:
	def __init__(self,title,priority,status):
		self.title = title
		self.priority = priority
		self.status = status
		
if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

    tasks = {int(k): v for k, v in tasks.items()}

    if tasks:
        tasks_id = max(tasks) + 1
    else:
        tasks_id = 1

else:
    tasks = {}
    tasks_id = 1


def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

found = True
while True:
	print('\n=====MENU=====')
	print(' 1. Add Task')
	print(' 2. View All Tasks')
	print(' 3. Update Task')
	print(' 4. Delete Task')
	print(' 5. Search Task')
	print(' 6. Mark Task as Completed')
	print(' 7. Filter tasks by priority')
	print(' 8. Show pending and completed task')
	print(' 9. Exit')
	
	user = int(input('Enter the option : '))
	
	if user == 1:
		print('\n====ADD TASK====')
		n = int(input('How much task :'))
		
		for _ in range(n):
			task_add = input('Enter the task name : ')
			task_priority = input(f'Enter the priority of task (low,medium,high) {task_add} : ')
			task_status = input(f'Enter the status of {task_add} : ')
			
			t = Task(task_add,task_priority,task_status)
			
			tasks[tasks_id] = {'Title' : t.title,
			'priority' : t.priority,
			'status' : t.status
			}
			
			tasks_id+=1
			save_tasks()
			
	elif user == 2:
		def view ():
			
			print('\n=====VIEW TASK=====')
			for i,a in tasks.items():
				print(f'{i} : {a}')
				
		view()
		
	elif user == 3:
		def update ():
			print('\n=====UPDATE TASK=====')
			update_task_id = int(input('Enter the task id for update : '))
			update_title = input('Enter the new title : ')
			update_priority = input('Enter the new priority  : ')
			update_status = input('Update the status : ')
			found = False
			
			for id,task in tasks.items():
				if id == update_task_id:
					found = True
					task['Title'] = update_title
					task['priority'] = update_priority
					task['status'] = update_status
					print('Update complete')
					save_tasks()
					
			if not found:
					found = False
					print('Task not found ')
		update()
		
	elif user == 4:
				def delete ():
					print('\n=====DELETE TASK=====')
					delete_id = int(input('Enter the task id for delete : '))
					found = False
					
					for id,value in tasks.items():
						if delete_id == id:
							found = True
							break
					
					if found:
							del tasks[delete_id]
							save_tasks()
							print('Deleted successfully')
					
					else:
							print('Not found')													
				delete()
				
				
	elif user == 5:
		def search ():
			print('\n====SEARCH TASK====')
			search_id = int(input('Enter the id :  '))
			found = False
			
			for id,value in tasks.items():
				if search_id == id:
					found = True
					print(f'{id} : {value}')
					break
					
			if not found:
					found = False
					print('Id not found')
					
		search()
		
	elif user == 6:
					def mark_complete():
						print('\n===MARK TASK COMPLETE===')
						mark_id = int(input('Enter the id : '))
						found = False
					
						for id,value in tasks.items():
							if mark_id == id:
								found = True
								tasks[mark_id]['status'] = 'Completed'
								save_tasks()
								print('Task marked as completed')
								break
						if not found :
							found = False
							print('Id not found')
					mark_complete()
					
	elif user == 7:
						def Filter_priority():
							
							user_priority = input('Enter the priority (low,medium,high) : ')
							found = False
							
							for id,value  in tasks.items():
								if user_priority == value['priority']:
									found = True
									print(f'===={user_priority} TASK====')
									print(f'{id} : {value}')
								
							if not found:
								found = False
								print('Not found')
								
						Filter_priority()
						
	elif user == 8:
							def show ():
								user_show = input('Enter the status (pending or completed) : ')
								found = False
								print(f'==={user_show} Task===')
								
								for id,value in tasks.items():
									if user_show == value['status']:
										found = True
										
										print(f'{id} : {value}')
								
								if not found:
									found = False
									print('Not found')
									
							show()
							
	elif user == 9:
							found = False
							if found == False:
								break
								
								
	else:
							print('Invalid option ')
							
								
								
					