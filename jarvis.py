import speech_recognition as sr
import pyttsx3
import pyautogui as py
import pygetwindow as pyw
import time
import os
import sys

engine = pyttsx3.init() # Initializing the engine for text-to-speech
engine.setProperty('rate', 200) # Setting rate of speech

# Initializing the Microphone and object for recognizing
mic = sr.Microphone()
r = sr.Recognizer()

# Listens from the laptop's mic and returns the recognized input in the form of string
def getVoiceCommand():
    with mic as source:
        audio = r.listen(source)
    speak("Audio Recorded, Analyzing...")
    try:
        inp = r.recognize_google(audio)
        return inp
    except:
        speak("Audio not recognized, please try again!")
        return 0

# Prints and speaks the string passed as parameter
def speak(string):
    print(string)
    engine.say(string)
    engine.runAndWait()

# Returns the window object as soon as the window opens
def checkIfWindowOpen(windowName):
    while True:
        window = pyw.getWindowsWithTitle(windowName)
        if window == []:
            continue
        else:
            return window[0]

# Opens 'Run' and runs the command passed as parameter
def cmd(command):
    py.hotkey('win', 'r')
    cmdWindow = checkIfWindowOpen('Run')
    time.sleep(2)   # Provides a halt of 2 seconds
    typing(command)
    py.press('enter')

# Mimics the keyboard activity by typing the string passed as parameter
def typing(string):
    py.typewrite(string, interval=0.1)

speak("Hello! How may I assist you?")

# Main Method
def main():
    # Keeps on accepting input until correct one is achieved
    while True:
        print("Speak..")
        inp = getVoiceCommand()
        if inp != 0:
            break
        
    print(f"You said: {inp}" )
    inp = inp.lower()   # Converts input to lowercase
    
    speak("Processing your Command")

    # Start of if tree
    if inp == "show my desktop":    # Minimizes all the windows
        py.hotkey('win', 'm')

    elif inp == "open command prompt":  # Opens command prompt
        cmd("cmd")

    elif inp[0:5] == "hello":         # Just responds back with a friendly gesture
        engine.say("Hey there! I hope you are having a lovely day!")
        engine.runAndWait()

    elif inp[0:7] == "goodbye":       # Ends the execution of the program
        engine.say("Thank you, see you soon!")
        engine.runAndWait()
        return 0

    elif inp == "take a note":          # Opens notepad and takes voice input
        cmd("notepad")
        notepadWindow = checkIfWindowOpen("Untitled - Notepad")
        time.sleep(2)
        while True:
            speak("What do you want to type?")
            print("Speak")
            newinp = getVoiceCommand()
            print(newinp)
            typing(newinp)
            py.press("enter")
            speak("Do you wish to add more?")
            ch = getVoiceCommand().lower()
            if ch == 'no':
                speak("Note Successfully Captured!")
                break

    elif inp[0:6] == "google":          # Opens chrome and performs a google search: 'Google Query'
        cmd("chrome")
        chromeWindow = checkIfWindowOpen('New Tab - Google Chrome')
        time.sleep(2)
        typing(inp[7:])
        py.press('enter')
        engine.say("Here are your results for " + inp[7:])
        engine.runAndWait()

    elif inp[0:4] == "play":            # Opens YouTube and plays a music: 'Play Songname'
        cmd("chrome")
        chromeWindow = checkIfWindowOpen('New Tab - Google Chrome')
        time.sleep(2)
        typing("youtube.com")
        py.press('tab')
        songname = inp[5:]
        typing(songname)
        py.press('enter')
        chromeWindow = checkIfWindowOpen(f'{songname} - YouTube - Google Chrome')
        time.sleep(2)
        py.press('tab')
        py.press('enter')

    elif inp == "close chrome":         # Closes one chrome window at a time
        windowlist = pyw.getAllTitles()
        string = 'Google Chrome'
        for i in range(len(windowlist)):
            if len(windowlist[i]) > len(string):
                chromeWindow = windowlist[i]
                end = chromeWindow[-1:-14:-1]   # Slices the string for 14 characters from behind
                if end[::-1] == 'Google Chrome':        # [::-1] for reversing the string
                    chromeWindows = pyw.getWindowsWithTitle(windowlist[i])
                    break

        for window in chromeWindows:
            window.close()

    else:
        speak("Unrecognized Command...")

    speak("Waiting for next command!")
    return 1

while main():
    continue

speak("Ending Execution")
