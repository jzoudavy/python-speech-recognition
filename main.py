import speech_recognition as sr

r = sr.Recognizer()
file_name=input ('File name: ')

sample_file = sr.AudioFile('audio_files/'+file_name)
with sample_file as source:
    audio = r.record(source)



#key already updated
speech=r.recognize_google(audio)
     
#speech=r.recognize_google_cloud(audio)


with open("output_files/"+file_name+".txt", "w") as text_file:
    text_file.write("Transribed text: {0}".format(speech))

