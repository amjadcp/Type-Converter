import pyttsx3 # pip install pyttsx3
friend = pyttsx3.init()
while True:
       word = input()
       friend.say(word)
       friend.runAndWait()
       
