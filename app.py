#validating python version
import sys
if sys.version_info[0] < 3:
    print("Error: You must use Python 3, try running $ python3 app.py or updating the python interpreter")

#their exercise code starts here
import json
from DataStructures import Queue

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode='FIFO', current_queue=['bob','kate','rick','romeo','juliet'])

def show_main_menu():
    print('''
What would you like to do (type a number and press enter)?
    - Type 1: For adding someone to the Queue.
    - Type 2: For removing someone from the Queue.
    - Type 3: For printing the current Queue state.
    - Type 4: To export the queue to the queue.json file.
    - Type 5: To import the queue from the queue.json file.
    - Type 6: To quit
    ''')
    response = input()
    return response

def enqueue():
    print('\nWho would you like to add to the queue?')
    person = input()
    queue.enqueue( person )
    ppl_in_front = queue.size() - 1 if queue._mode == 'FIFO' else 0
    qty = 'is 1 person' if ppl_in_front == 1 else f'are {ppl_in_front} people'
    print(f'{person} added to queue. There {qty} before it.')

def dequeue():
    person = queue.dequeue()
    print(f'{person} has been removed from queue')
        
def print_queue():
    print("Printing the entire list...")
    print(queue.get_queue())

def export_queue():
    print('Exporting queue to json file...')
    jfile = open('queue.json','w')
    json.dump( queue.get_queue(), jfile )
    jfile.close()
    print('json file has been created successfully.')

def import_queue():
    print('Importing queue from json file...')
    jfile = open('queue.json','r')
    global queue
    queue = Queue( mode='FIFO', current_queue=json.load(jfile) )
    jfile.close()
    print_queue()

def start():
    
    print("\nHello, this is the Command Line Interface for a Queue Managment application.")
    while True:
        
        option = show_main_menu()
        
        try: #converting the user input into an integer
            option = int(option)
        except ValueError:
            print("Invalid option "+str(option))

        # add your options here using conditionals (if)
        if option == 1:
            enqueue()
        elif option == 2:
            dequeue()
        elif option == 3:
            print_queue()
        elif option == 4:
            export_queue()
        elif option == 5:
            import_queue()
        elif option == 6:
            print("Adios Amigo!")
            return None
        else:
            print("Invalid option "+str(option))

    
start()