import speech_recognition as sr
import json

r = sr.Recognizer()
file_name=input ('File name: ')

sample_file = sr.AudioFile('audio_files/'+file_name)
with sample_file as source:
    audio = r.record(source)



#key already updated
#speech=r.recognize_google(audio,key='AIzaSyANo-1hs6HOgUKg3Cg8KxB_JhjWlp-gR8g')

with open("/home/davy/CloudSpeech_Key.json", "r") as key:
   CloudSpeech_Key=json.load(key)


speech=r.recognize_google_cloud(audio)

        

with open("output_files/"+file_name+".txt", "w") as text_file:
    text_file.write("Transribed text: {0}".format(speech))

