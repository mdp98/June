import sys
import os

def speak(text):
    os.system("espeak '"+text+"'")

if __name__ == "__main__":
    main()
