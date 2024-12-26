import pyjokes
from ai import AI


quesadilla = AI()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    quesadilla.say(funny)

command = ""
while True and command != "goodbye":
    command = quesadilla.listen()
    print("command was:",command)

    if command == "tell me a joke":
        joke()

quesadilla.say("Goodbye, I'm going to sleep now")