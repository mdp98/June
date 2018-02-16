import tts
import postag
import wiki 
import lights 
import socket
import fan
import kill
import sys

HOST = '192.168.43.13'
PORT = 8800

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'

#Bind socket to Host and Port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1]
    sys.exit()

print 'Socket Bind Success!'


#listen(): This method sets up and start TCP listener.
s.listen(10)
print 'Socket is now listening'

while 1:
    command = ''
    conn, addr = s.accept()
    print 'Connect with ' + addr[0] + ':' + str(addr[1])
    command = conn.recv(64)
    print command
    if command=='':
        continue
    tags = postag.postag(command)
    print(tags)

    if ('what', 'WP') in tags:
        tts.speak("Searching ....")
        wiki.getInfo(command)
    if 'lights' or 'light' in command:
        if 'on' in command:
            lights.on()
        if 'off' in command:
            lights.off()
    if 'fan' in command:
        if 'on' in command:
            fan.on()
        if 'off' in command:
            fan.off()
    if 'all kill' in command:
        kill.killall()
s.close()



