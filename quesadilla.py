import pyjokes
from ai import AI
from todo import Todo, Item

quesadilla = AI()
todo = Todo()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    quesadilla.say(funny)

def add_todo()->bool:
    item=Item()
    quesadilla.say("Tell me what to add to the list")
    try:
        item.title=quesadilla.listen()
        todo.new_item(item)
        message="Added " + item.title
        quesadilla.say(message)
        return True
    except:
        print("oops there was an error adding the task to the todo list")
        return False
    
def list_todos():
    if todo.__length__() > 0:
        quesadilla.say("Your to do's are")
        for item in todo:
            quesadilla.say(item.title)
    else:
        print("The todo list is empty")

def remove_todo()->bool:
    quesadilla.say("Which task do you want me to remove?")
    try:
        item_title = quesadilla.listen()
        todo.remove_item(title=item_title)
        message="Removed " + item_title
        quesadilla.say(message)
        return True
    except:
        print("oops there was an error removing the task from the todo list")
        return False



# ------------ MAIN LOOP ------------
command = ""
while True and command != "goodbye":
    try:
        #wait for a command and process it 
        command = quesadilla.listen()
        command = command.lower()
    except:
        print("oops there was an error")
        command=""
    print("command was:",command)
 
    #command options 
    # (i know it's very unoptimized and stupid doing if-if-if 
    # without applying any mathematical solution, 
    # my man i'm just getting started step by step dayum)
    if command == "tell me a joke":
        joke()
        command=""
    if command in ["add to-do","add to do","add a task for today"]:
        add_todo()
        command=""
    if command in ["list my to do's","list my tasks","list my tasks for today","what do I have to do today?"]:
        list_todos()
        command=""
    if command in ["remove todo","remove task","mark done","I finished a task","remove to-do","remove todo from the list"]:
        remove_todo()
        command=""

quesadilla.say("Goodbye!")