import wikipedia
import tts

def getInfo(command):
    data = wikipedia.summary(command)
    data= data.split(".",2)[0:2]
    print(data)
    for i in data:
        tts.speak(i)

if __name__ == "__main__":
    main()
