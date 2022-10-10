import speech_recognition as sr # need the module SpeechRecognition, pyAudio install it by(pip install  SpeechRecognition, pyAudio)
import pyttsx3
# python3 -m speech_recognition - find threshold

listener = sr.Recognizer()
listener.energy_threshold = 11115.33955353187 
listener.dynamic_energy_threshold = True
friend = pyttsx3.init()
while True:
 with sr.Microphone() as source:
    print("say somthing.....")
    voice = listener.listen(source)
    identify = listener.recognize_google(voice)
    print(identify)
