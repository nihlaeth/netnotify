import socket
import sys
import pynotify


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Failed to create socket:", msg
    syst.exit();
print "Created socket"
port = 5757
s.bind(("", port))
print "Now listening on port", port

s.listen(10)
pynotify.init("Python notification Daemon")
while 1:
    client, address = s.accept()
    data = client.recv(4096)
    print "Got connection from", address
    print data
    datalist = data.split(":", 1)
    title = datalist[0]
    try:
        body = datalist[1]
    except IndexError:
        print "No notification body received, using title"
        body = title
    n = pynotify.Notification(title, body)
    n.show()
    client.close()


