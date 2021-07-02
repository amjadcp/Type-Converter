import speech_recognition as sr # need the module SpeechRecognition, pyAudio install it by(pip install  SpeechRecognition, pyAudio)

listener = sr.Recognizer()
friend = pyttsx3.init()
while True:
 with sr.Microphone() as source:
    print("say somthing.....")
    voice = listener.listen(source)
    identify = listener.recognize_google(voice)
    print(identify)
