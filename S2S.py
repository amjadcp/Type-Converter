import speech_recognition as sr # need the module SpeechRecognition, pyAudio and pyttsx3 install it by(pip install  SpeechRecognition, pyAudio, pyttsx3)
import pyttsx3

listener = sr.Recognizer()
friend = pyttsx3.init()
while True:
 with sr.Microphone() as source:
    print("say somthing.....")
    voice = listener.listen(source)
    identify = listener.recognize_google(voice)
    word = identify
    friend.say(word)
    friend.runAndWait()




