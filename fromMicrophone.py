'''
This reads the data from the Microphone and converts into the textData and
renders out the text 

'''
import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something: ")
    audioData = r.listen(source)
    print("\n[Recognizing]...")
    try:
        textData = r.recognize_google(audioDat)
        print("You said : ",textData)
    except:
        print("Could Not recognize your voice")


