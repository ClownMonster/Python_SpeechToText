'''
Gets the Text out of an English Audio File

'''
import speech_recognition as sr 

r = sr.Recognizer()

def convert_to_text(audioFile):
    with sr.AudioFile(audioFile) as source:
        audioData = r.record(source)
        text = r.recognize_google(audioData)
        print("\ntext : ", text)


if __name__ == "__main__":
    file_path = input("Enter the realtive path to audio file: ") 
    # 16-122828-0002.wav is the audio file u can use any
    convert_to_text(file_path)