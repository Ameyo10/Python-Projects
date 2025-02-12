#Making Lists
task=[]
incompleted=[]
completed=[]

#Adding a new task
def new_task(new):
    task.append(new)
    incompleted.append(new)

#When a task is completed
def complete():
    print(' The incompleted tasks are: ')
    for i in incompleted:
        print(i, end = '\n')
    
    t = input('Enter the name of the completed task: ')
    incompleted.remove(t)
    completed.append(t)
    print(' The incompleted tasks are: ')
    for i in incompleted:
        print(i, end = '\n')
        
    print(' The completed tasks are: ')
    for i in completed:
        print(i, end = '\n')

#At the Start of the Day or in case of addition of a new task
def start():
    choice = 1
    while choice == 1:
        new = input('Enter New Task: ')
        new_task(new)
        c = input('Do you need to enter a new task? y/n')
        if c=='n':
            choice = 0
    print (' The tasks for the day are: ')
    for i in task:
        print(i,end = '\n')        

#choices given
def choices():
    print('''What would you like to do?
    1. Add a new task
    2. Update the completion of a task''')
    c = int(input('Enter the number associated with the action'))
    if c==1:
        start()
    elif c==2:
        complete()
x = 1
while x == 1:
        c = input('Do you need to enter a new task? y/n')
        choices()
        if c=='n':
            x = 0
            break