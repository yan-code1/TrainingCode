import threading
from time import sleep

import speech_recognition as sr
import os

def file_walker(path):
    file_list = []
    for root, dirs, files in os.walk(path):  # 生成器
        for fn in files:
            p = str(root + '/' + fn)
            file_list.append(p)
    file_list.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    print(file_list)
    return file_list
def recThread(audio_file_path,i,captions):
    r = sr.Recognizer()
    audioFile = sr.AudioFile(audio_file_path)
    with audioFile as source:
        audio = r.record(source)
        # r.recognize_sphinx(audio, language='zh_CN')
        # 选择语言
        # 选择翻译片段
        try:
            text = r.recognize_google(audio)
            captions[i] = text
            # print("%d said: "% i, text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service" + format(e))


# use microphone
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# use audio file
files_path = './chunks'
audioFileAll = file_walker(files_path)
captions = [None for _ in range(len(audioFileAll))]
Threads = []
for i in range(len(audioFileAll)):
    audio_file_path = audioFileAll[i]
    print('input:',audio_file_path)
    t = threading.Thread(target=recThread,args=(audio_file_path,i,captions,))
    sleep(0.1)
    Threads.append(t)
    t.start()
print('waiting for finishing')
for t in Threads:
    t.join()
for i in range(len(captions)):
    print("%d said: " % i, captions[i])




# r.recognize_sphinx(audio, language='zh_CN')
# 选择语言
# 选择翻译片段
