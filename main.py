import speech_recognition as sr;
import os
import time


#https://realpython.com/python-speech-recognition/

def recognizeVoice():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(3)
        print("Start recording!")
        audio = r.listen(source,None,10)
        print("Stop recording!")
    # Speech recognition using Google Speech Recognition


        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            strin=r.recognize_google(audio)
            print("You said: " + strin)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return strin


def executeCommandSetVolume(com):
    os.system("setvol "+com)

def executeSleepLaptop():
    os.system("RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0")

def executeScreenshot():
    os.system("nircmd.exe savescreenshot screen1.png")

def executeSong():
    os.system("start song.mp3")
    time.sleep(6)

def shutDownMonitor():
    os.system("nircmd.exe monitor off")

def executeSayHi():
    os.system("start songHello.mp3")
    time.sleep(6)

def executeGoodbye():
    os.system("start songBye.mp3")
    time.sleep(8)

def executeWait():
    time.sleep(10)

def clearBin():
    os.system("nircmd.exe emptybin")


def getVolumeFromCommand(strin):
    words = str.split(strin)
    for w in words:
        if w.isdecimal():
            print(w)
            break;
    if findMute(strin) == 1:
        return "0";
    else:
        if w.isdecimal():
            return w
        else:
            return -1

def findMute(strin):
    words = str.split(strin)
    for w in words:
        if w == "mute":
            return 1
    return 0

def findSleepLaptop(strin):
    words = str.split(strin)
    for w in words:
        if w == "sleep":
            return 1
    return 0

def findScreenShot(strin):
    words = str.split(strin)
    for w in words:
        if w == "screenshot":
            return 1
    return 0

def findThankYou(strin):
    words = str.split(strin)
    for w in words:
        if w == "thanks" or w == "thank":
            return 1
    return 0;

def findMonitor(strin):
    words = str.split(strin)
    for w in words:
        if w == "monitor":
            return 1
    return 0

def findHello(strin):
    words = str.split(strin)
    for w in words:
        if w == "hi" or w == "hello":
            return 1
    return 0

def findGoodbye(strin):
    words = str.split(strin)
    for w in words:
        if w =="bye" or w == "goodbye":
            return 1
    return 0

def findWait(strin):
    words = str.split(strin)
    for w in words:
        if w == "wait":
            return 1
    return 0

def findRecycle(strin):
    words = str.split(strin)
    for w in words:
        if w =="recycle" or w == "bin":
            return 1
    return 0

#Commands :
    #hi - to say hello
    #setvolume valoare
    #mute
    #take screenshot - face screenshot
    #thanks or thank you
    #wait - asteapta 10 secunde
    #clear recycle bin - curata cosul
    #turn off monitor - stinge monitorul
    #sleep - pune laptopul pe sleep
    #goodbye - isi ia la revedere

if __name__ == '__main__':
    stop = 0
    while stop == 0:
        strin=recognizeVoice()
        if findHello(strin):
            executeSayHi()
        volume = getVolumeFromCommand(strin)
        if volume != -1:
            executeCommandSetVolume(volume)
        if findSleepLaptop(strin):
            executeSleepLaptop()
        if findScreenShot(strin):
            executeScreenshot()
        if findThankYou(strin):
            executeSong()
        if findWait(strin):
            executeWait()
        if findMonitor(strin):
            shutDownMonitor()
        if findRecycle(strin):
            clearBin()
        if findGoodbye(strin):
            executeGoodbye()
            stop = 1
