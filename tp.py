import speech_recognition as sr
import pyttsx3
import pyautogui as py
import time

engine = pyttsx3.init('sapi5')
print("Hello Sir! How may I assist you?")
engine.say("Hello Sir! How may I assist you?")
engine.runAndWait()
mic = sr.Microphone()
r = sr.Recognizer()

def minimize():
    py.hotkey('win', 'm')

def cmd(command):
    py.hotkey('win', 'r')
    time.sleep(0.5)
    typing(command)
    py.keyDown('enter')
    py.keyUp('enter')

def typing(string):
    for s in string:
        py.keyDown(s)
        py.keyUp(s)

def main():
    print("Speak..")
    with mic as source:
        inp = r.recognize_google(r.listen(source)).lower()
    print(f"You said: {inp}" )
    print("Processing your command")
    engine.say("Processing your command")
    engine.runAndWait()
    if inp == "minimise all windows":
        minimize()

    elif inp == "open command prompt":
        cmd("cmd")

    elif inp == "hello jarvis":
        engine.say("Hello Sir!")
        engine.runAndWait()

    elif inp == "open recent":
        py.hotkey('alt', 'tab')

    elif inp == "goodbye jarvis":
        return 0

    elif inp == "open notepad":
        cmd("notepad")
        engine.say("What do you want to type?")
        engine.runAndWait()
        print("speak")
        with mic as source:
            newinp = r.recognize_google(r.listen(source))
        print(newinp)
        typing(newinp)

    elif inp[0:6] == "google":
        cmd("chrome")
        time.sleep(2)
        py.hotkey('ctrl', 'shift', 'n')
        time.sleep(0.5)
        typing(inp[7:])
        py.keyDown('enter')
        py.keyUp('enter')
        engine.say("Here are your results for " + inp[7:])
        engine.runAndWait()

    elif inp[0:4] == "play":
        cmd("chrome")
        time.sleep(2)
        py.hotkey('ctrl', 'shift', 'n')
        time.sleep(0.5)
        typing("youtube")
        py.keyDown('tab')
        py.keyUp('tab')
        typing(inp[5:])
        py.keyDown('enter')
        py.keyUp('enter')
        time.sleep(4)
        py.click(400, 300)

    else:
        print("Unrecognized Command...")
        engine.say("Unrecognized Command")
        engine.runAndWait()

    print("Waiting for next Command")
    engine.say("Waiting for next Command")
    engine.runAndWait()
    return 1

while main():
    continue

print("Ending Execution. Thank You")
engine.say("Ending Execution, Thank You")
engine.runAndWait()


    
